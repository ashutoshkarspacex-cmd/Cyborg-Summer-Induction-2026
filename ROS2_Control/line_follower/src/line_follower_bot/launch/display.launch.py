from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg=get_package_share_directory('line_follower_bot')
    urdf=os.path.join(pkg,'urdf','line_follower.urdf')
    with open(urdf) as f:
        desc=f.read()
    return LaunchDescription([
        Node(package='robot_state_publisher',
             executable='robot_state_publisher',
             parameters=[{'robot_description':desc}]),
        Node(package='joint_state_publisher_gui',
             executable='joint_state_publisher_gui'),
        Node(package='rviz2',
             executable='rviz2')
    ])
