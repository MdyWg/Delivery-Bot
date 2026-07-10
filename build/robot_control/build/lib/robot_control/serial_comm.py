import math
import threading
import serial
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray

# TODO: firmware reports left_speed/right_speed as encoder counts per 100ms.
# Confirm counts-per-revolution (post-gearbox, at the wheel) from the
# motor/encoder datasheet and replace this placeholder before trusting odometry.
TICKS_PER_REV = 1.0


class SerialComm(Node):
    def __init__(self):
        super().__init__('serial_comm')

        self.declare_parameter('port', '/dev/ttyAMA0')
        self.declare_parameter('baud_rate', 115200)
        port = self.get_parameter('port').get_parameter_value().string_value
        baud_rate = self.get_parameter('baud_rate').get_parameter_value().integer_value

        try:
            self.ser = serial.Serial(port, baud_rate, timeout=1)
            self.get_logger().info(f'Opened serial port {port} at {baud_rate} baud')
        except serial.SerialException as e:
            self.get_logger().fatal(f'Failed to open serial port: {e}')
            raise

        self.wheel_pub = self.create_publisher(Float64MultiArray, '/wheel_velocities', 10)

        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        threading.Thread(target=self._read_loop, daemon=True).start()

    def _read_loop(self):
        while rclpy.ok():
            try:
                line = self.ser.readline().decode('utf-8').strip()
            except (serial.SerialException, UnicodeDecodeError) as e:
                self.get_logger().warn(f'Serial read error: {e}')
                continue

            if not line:
                continue

            # firmware format: "CCR1,CCR2,left_count,right_count,left_speed,right_speed"
            # left_speed/right_speed are encoder counts per 100ms.
            parts = line.split(',')
            if len(parts) != 6:
                continue

            try:
                left_speed = int(parts[4])
                right_speed = int(parts[5])
            except ValueError:
                self.get_logger().warn(f'Could not parse encoder line: {line}')
                continue

            counts_per_sec_left = left_speed * 10.0
            counts_per_sec_right = right_speed * 10.0
            left_rad_s = (counts_per_sec_left / TICKS_PER_REV) * 2 * math.pi
            right_rad_s = (counts_per_sec_right / TICKS_PER_REV) * 2 * math.pi

            msg = Float64MultiArray()
            msg.data = [left_rad_s, right_rad_s]
            self.wheel_pub.publish(msg)

    def cmd_vel_callback(self, msg: Twist):
        # convert Twist to left/right wheel velocities for differential drive
        wheel_radius = 0.0325     # metres
        wheel_separation = 0.275  # metres

        vx = msg.linear.x
        vth = msg.angular.z

        left_ms = vx - (vth * wheel_separation / 2.0)
        right_ms = vx + (vth * wheel_separation / 2.0)

        left_rad_s = left_ms / wheel_radius
        right_rad_s = right_ms / wheel_radius

        # TODO: firmware doesn't parse RX commands yet -- this wire format is a
        # placeholder until the STM32 side implements a command parser.
        command = f'V {left_rad_s:.3f} {right_rad_s:.3f}\n'
        try:
            self.ser.write(command.encode('utf-8'))
        except serial.SerialException as e:
            self.get_logger().warn(f'Serial write error: {e}')

    def destroy_node(self):
        if self.ser.is_open:
            self.ser.write(b'V 0.000 0.000\n')
            self.ser.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SerialComm()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
