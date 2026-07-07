from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share     = FindPackageShare(package='robot_navigation').find('robot_navigation')
    slam_config   = os.path.join(pkg_share, 'config', 'slam_toolbox.yaml')
    nav2_params   = os.path.join(pkg_share, 'config', 'nav2_params.yaml')

    depth_to_scan_node = Node(
        package='depthimage_to_laserscan',
        executable='depthimage_to_laserscan_node',
        name='depthimage_to_laserscan',
        parameters=[{
            'scan_height': 5,
            'output_frame': 'camera_link',
            'range_min': 0.1,
            'range_max': 3.5,
        }],
        remappings=[
            ('depth',            '/depth/image_raw'),
            ('depth_camera_info', '/depth/camera_info'),
            ('scan',             '/scan'),
        ]
    )

    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[slam_config, {'use_sim_time': LaunchConfiguration('use_sim_time')}],
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('nav2_bringup'), '/launch/navigation_launch.py'
        ]),
        launch_arguments={
            'params_file':   nav2_params,
            'use_sim_time':  LaunchConfiguration('use_sim_time'),
        }.items()
    )

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    return LaunchDescription([
        DeclareLaunchArgument(name='use_sim_time', default_value='false',
                                            description='Flag to enable use_sim_time'),
        robot_localization_node,
        depth_to_scan_node,
        slam_toolbox_node,
        nav2,
    ])