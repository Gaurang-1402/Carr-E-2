from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    package_filepath = get_package_share_directory('carr-e-2')
    joy_params = os.path.join(package_filepath, 'config', 'joystick_params.yaml')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params]
    )

    return LaunchDescription(
        [
            joy_node
        ]
    )

