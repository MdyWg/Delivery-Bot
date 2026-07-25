from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EqualsSubstitution, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share = FindPackageShare('robot_navigation')
    use_sim_time = LaunchConfiguration('use_sim_time')
    localization_mode = LaunchConfiguration('localization_mode')
    map_yaml = LaunchConfiguration('map')
    localization_config = PathJoinSubstitution([pkg_share, 'config', 'ekf.yaml'])
    slam_config = PathJoinSubstitution([pkg_share, 'config', 'slam_params.yaml'])
    nav2_params = PathJoinSubstitution([pkg_share, 'config', 'nav2_params.yaml'])

    depth_to_scan_node = Node(
        package='depthimage_to_laserscan',
        executable='depthimage_to_laserscan_node',
        name='depthimage_to_laserscan',
        parameters=[{
            'scan_height': 10,
            'output_frame': 'camera_link',
            'range_min': 0.1,
            'range_max': 4.0,
            'use_sim_time': use_sim_time
        }],
        remappings=[
            ('depth', 'depth/image_raw'),
            ('depth_camera_info', 'depth/camera_info'),
        ]
    )

    slam_toolbox_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('slam_toolbox'), '/launch/online_async_launch.py'
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'slam_params_file': slam_config  
        }.items(),
        condition=IfCondition(EqualsSubstitution(localization_mode, 'slam'))
    )

    amcl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('nav2_bringup'), '/launch/localization_launch.py'
        ]),
        launch_arguments={
            'map': map_yaml,
            'use_sim_time': use_sim_time,
        }.items(),
        condition=IfCondition(EqualsSubstitution(localization_mode, 'amcl'))
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('nav2_bringup'), '/launch/navigation_launch.py'
        ]),
        launch_arguments={
            'params_file':   nav2_params,
            'use_sim_time':  use_sim_time,
        }.items()
    )

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[localization_config, {'use_sim_time': use_sim_time}],
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false', description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument('localization_mode', default_value='slam', description='Choose between slam or amcl for localization'),
        DeclareLaunchArgument('map', default_value=PathJoinSubstitution([pkg_share, 'maps', 'map.yaml']), description='Full path to map file to load'),
        robot_localization_node,
        depth_to_scan_node,
        slam_toolbox_node,
        amcl,
        nav2,
    ])