import threading
import serial
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


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

            parts = line.split()
            if len(parts) == 5 and parts[0] == 'E':
                try:
                    fl, fr, rl, rr = float(parts[1]), float(parts[2]), \
                                    float(parts[3]), float(parts[4])
                    return [fl, fr, rl, rr]
                except ValueError:
                    print(f'Could not parse encoder line: {line}')
            return 

    def cmd_vel_callback(self, msg: Twist):
        # convert Twist to individual wheel velocities for skid steer
        wheel_radius    = 0.0325    # metres
        wheel_separation = 0.275  # metres

        vx  = msg.linear.x
        vth = msg.angular.z

        left_ms  = vx - (vth * wheel_separation / 2.0)
        right_ms = vx + (vth * wheel_separation / 2.0)

        fl = rl = left_ms  / wheel_radius  # rad/s
        fr = rr = right_ms / wheel_radius  # rad/s

        # send to STM32: "V fl fr rl rr\n"
        command = f'V {fl:.3f} {fr:.3f} {rl:.3f} {rr:.3f}\n'
        try:
            self.ser.write(command.encode('utf-8'))
        except serial.SerialException as e:
            self.get_logger().warn(f'Serial write error: {e}')

    def destroy_node(self):
        self._running = False
        if self.ser.is_open:
            self.ser.write(b'V 0.000 0.000 0.000 0.000\n')
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
