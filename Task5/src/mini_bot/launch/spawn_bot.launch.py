'''
*****************************************************************************************
*
*        =============================================
*                  Cyborg ROS Task-2
*        =============================================
*
*  Filename:         spawn_bot.launch.py
*  Description:      Spawn bot in Ignition Gazebo Fortress with ros2_control
*
*****************************************************************************************
'''

from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node

import os
import xacro

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    share_dir = get_package_share_directory("mini_bot")

    xacro_file = os.path.join(
        share_dir,
        "urdf",
        "mini_bot_1.urdf.xacro"
    )

    robot_description = xacro.process_file(xacro_file).toxml()

    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description,
                "use_sim_time": True,
            }
        ],
    )

    # Spawn robot into Ignition Gazebo
    spawn_robot = ExecuteProcess(
        cmd=[
            "ros2",
            "run",
            "ros_gz_sim",
            "create",
            "-name",
            "mini_bot",
            "-topic",
            "robot_description",
        ],
        output="screen",
    )

    # Controller spawner: Joint State Broadcaster
    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    # Controller spawner: Wheel Velocity Controller
    wheel_velocity_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["wheel_velocity_controller"],
        output="screen",
    )

    # Start JSB after robot is spawned
    load_joint_state_broadcaster = RegisterEventHandler(
        OnProcessExit(
            target_action=spawn_robot,
            on_exit=[joint_state_broadcaster],
        )
    )

    # Start velocity controller after JSB
    load_velocity_controller = RegisterEventHandler(
        OnProcessExit(
            target_action=joint_state_broadcaster,
            on_exit=[wheel_velocity_controller],
        )
    )

    return LaunchDescription([
        robot_state_publisher,
        spawn_robot,
        load_joint_state_broadcaster,
        load_velocity_controller,
    ])