from launch import LaunchDescription
from launch_ros.actions import Node

import os
import xacro

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    mini_bot_share = get_package_share_directory("mini_bot")

    xacro_file = os.path.join(
        mini_bot_share,
        "urdf",
        "mini_bot_1.urdf.xacro"
    )

    robot_description = xacro.process_file(xacro_file).toxml()

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description
            }
        ]
    )

    joint_state_publisher = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription([
        joint_state_publisher,
        robot_state_publisher,
        rviz
    ])