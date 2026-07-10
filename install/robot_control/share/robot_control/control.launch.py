from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    odom_publisher = Node(
        package='robot_control',
        executable='odom_publisher'
    )
    serial_comm = Node(
        package='robot_control',
        executable='serial_comm'
    )

    return LaunchDescription([
        serial_comm,
        odom_publisher
    ])