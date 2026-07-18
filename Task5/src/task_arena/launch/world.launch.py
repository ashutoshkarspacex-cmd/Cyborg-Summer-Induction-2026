import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import (
    get_package_share_directory,
    get_package_prefix
)

pkg_name = 'task_arena'


def generate_launch_description():

    pkg_models_dir = get_package_share_directory(pkg_name)
    install_dir = get_package_prefix(pkg_name)

    world_file = os.path.join(
        pkg_models_dir,
        'worlds',
        'gazebo.world'
    )

    model_path = os.path.join(
        pkg_models_dir,
        'models'
    )

    sensor_bridge_yaml = os.path.join(
        pkg_models_dir,
        "config",
        "sensor_bridge.yaml"
    )

    if 'IGN_GAZEBO_RESOURCE_PATH' in os.environ:
        os.environ['IGN_GAZEBO_RESOURCE_PATH'] += ':' + model_path
    else:
        os.environ['IGN_GAZEBO_RESOURCE_PATH'] = model_path

    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            '-r',
            world_file
        ],
        output='screen'
    )

    sensor_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        parameters=[{
            "config_file": sensor_bridge_yaml
        }],
        output="screen",
    )

    return LaunchDescription([
        gazebo,
        sensor_bridge
    ])