import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    urdf_path = os.path.join(
        FindPackageShare('robot_description').find('robot_description'),
        'description', 'robot_description.urdf'
    )

    rviz_config_path = os.path.join(
        FindPackageShare('robot_description').find('robot_description'),
        'rviz', 'config.rviz'
    )

    nav_launch = os.path.join(
        FindPackageShare('robot_navigation').find('robot_navigation'),
        'launch', 'navigation.launch.py'
    )

    # publishes /tf and /tf_static for the robot links
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path]),
            'use_sim_time': use_sim_time,
        }]
    )

    odom_publisher = Node(
        package='robot_control',
        executable='odom_publisher',
        name='odom_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # publishes zero joint states for continuous joints (wheels) until
    # real encoder data is available via ros2_control
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path]),
            'use_sim_time': use_sim_time,
        }]
    )

    camera = Node(
        package='robot_vision',
        executable='arducam_tof',
        name='arducam_tof',
        output='screen',
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path],
    )

    # EKF node (robot_localization) — fuses /odom into /odometry/filtered
    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav_launch),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='false',
            description='Use simulation clock if true'
        ),
        robot_state_publisher,
        joint_state_publisher,
        odom_publisher,
        camera,
        navigation,
        rviz,
    ])
