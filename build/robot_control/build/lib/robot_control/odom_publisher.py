from math import *
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
import tf_transformations
from geometry_msgs.msg import Quaternion, TransformStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray

class OdomPublisher(Node):
    def __init__(self):
        super().__init__('odom_publisher')
        self.odom_publisher = self.create_publisher(Odometry, 'odom', 10)
        self.odom_broadcaster = TransformBroadcaster(self)

        self.x = 0.0
        self.y = 0.0
        self.th = 0.0

        self.vx  = 0.0
        self.vy  = 0.0
        self.vth = 0.0

        self.wheel_radius     = 0.0325
        self.wheel_separation = 0.275
        
        self.last_time = self.get_clock().now()

        self.create_subscription(
            Float64MultiArray, '/wheel_velocities', self.wheel_callback, 10)

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    
    def wheel_callback(self, msg):
        left_rad_s, right_rad_s = msg.data

        left_ms  = left_rad_s * self.wheel_radius
        right_ms = right_rad_s * self.wheel_radius

        self.vx  = (right_ms + left_ms) / 2.0
        self.vy  = 0.0
        self.vth = (right_ms - left_ms) / self.wheel_separation

    def timer_callback(self):
        current_time = self.get_clock().now()

        dt = (current_time - self.last_time).nanoseconds / 1e9
        delta_x = (self.vx * cos(self.th) - self.vy * sin(self.th)) * dt
        delta_y = (self.vx * sin(self.th) + self.vy * cos(self.th)) * dt
        delta_th = self.vth * dt

        self.x += delta_x
        self.y += delta_y
        self.th += delta_th

        odom_quat_arr = tf_transformations.quaternion_from_euler(0, 0, self.th)
        odom_quat = Quaternion()
        odom_quat.x = odom_quat_arr[0]
        odom_quat.y = odom_quat_arr[1]
        odom_quat.z = odom_quat_arr[2]
        odom_quat.w = odom_quat_arr[3]

        odom_trans = TransformStamped()
        odom_trans.header.stamp = current_time.to_msg()
        odom_trans.header.frame_id = 'odom'
        odom_trans.child_frame_id = 'base_link'

        odom_trans.transform.translation.x = self.x
        odom_trans.transform.translation.y = self.y
        odom_trans.transform.translation.z = 0.0
        odom_trans.transform.rotation = odom_quat

        self.odom_broadcaster.sendTransform(odom_trans)

        odom_msg = Odometry()
        odom_msg.header.stamp = current_time.to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'
        
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = 0.0
        odom_msg.pose.pose.orientation = odom_quat

        odom_msg.twist.twist.linear.x = self.vx
        odom_msg.twist.twist.linear.y = self.vy
        odom_msg.twist.twist.angular.z = self.vth

        self.odom_publisher.publish(odom_msg)
        self.last_time = current_time

def main(args=None):
    rclpy.init(args=args)
    odom_publisher = OdomPublisher()
    rclpy.spin(odom_publisher)
    odom_publisher.destroy_node()
    rclpy.shutdown()