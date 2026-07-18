from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    pkg = get_package_share_directory("line_follower_bot")
    gz_pkg = get_package_share_directory("ros_gz_sim")

    xacro_file = os.path.join(
        pkg,
        "urdf",
        "line_follower.urdf.xacro"
    )

    robot_description = {
        "robot_description":
            xacro.process_file(xacro_file).toxml()
    }

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                gz_pkg,
                "launch",
                "gz_sim.launch.py"
            )
        ),
        launch_arguments={
            # -r = start simulation immediately (not paused)
            "gz_args": "-r " + os.path.join(
                pkg,
                "worlds",
                "line_world.sdf"
            )
        }.items()
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen"
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic", "robot_description",
            "-name", "line_follower",
            "-x", "0.0",
            "-y", "0.0",
            "-z", "5.15"
        ]
    )

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ],
        output="screen"
    )

    diff_drive_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "diff_drive_controller",
            "--controller-manager",
            "/controller_manager"
        ],
        output="screen"
    )

    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        output="screen",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            "/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist"
        ]
    )

    return LaunchDescription([

        gazebo,

        robot_state_publisher,

        spawn_robot,

        RegisterEventHandler(
            OnProcessExit(
                target_action=spawn_robot,
                on_exit=[joint_state_broadcaster]
            )
        ),

        RegisterEventHandler(
            OnProcessExit(
                target_action=joint_state_broadcaster,
                on_exit=[diff_drive_controller]
            )
        ),
        bridge,

    ])