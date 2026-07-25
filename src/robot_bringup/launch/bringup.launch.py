import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    robot_control = FindPackageShare('robot_control')
    robot_description = FindPackageShare('robot_description')
    robot_navigation = FindPackageShare('robot_navigation')
    robot_vision = FindPackageShare('robot_vision')

    camera = Node(
        package='robot_vision',
        executable='arducam_tof',
        name='arducam_tof',
        output='screen',
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([robot_navigation, 'launch', 'navigation.launch.py'])
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([robot_description, 'launch', 'display.launch.py'])
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([robot_control, 'launch', 'control.launch.py'])
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='false',
            description='Use simulation clock if true'
        ),
        camera,
        control,
        description,
        navigation,
    ])
