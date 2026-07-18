#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    urdf_file = '/home/the_wizard_of_nowhere/Cyborg-Summer-Induction-2026/Task4/Task4b/linefollower.urdf'
    
    with open(urdf_file, 'r') as infp:
        robot_description_config = infp.read()
        
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config, 'use_sim_time': True}]
    )

    gazebo_ros_share = get_package_share_directory('gazebo_ros')
    gazebo_server_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_share, 'launch', 'gazebo.launch.py')
        )
    )

    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description', 
            '-entity', 'line_follower_bot',
            '-x', '0.0', '-y', '0.0', '-z', '0.1' 
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo_server_client,
        robot_state_publisher_node,
        spawn_entity_node
    ])

if __name__ == '__main__':
    import launch
    import launch.launch_service
    ls = launch.launch_service.LaunchService()
    ls.include_launch_description(generate_launch_description())
    ls.run()