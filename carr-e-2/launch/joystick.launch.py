from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    package_filepath = get_package_share_directory('carr-e-2')
    
    joystick_params = os.path.join(package_filepath, 'config', 'joystick_params.yaml')
    teleop_params = os.path.join(package_filepath, 'config', 'teleop_params.yaml')


    joystick_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joystick_params]
    )


    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        parameters=[teleop_params],
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
    )


    return LaunchDescription(
        [
            joystick_node,
            teleop_node
        ]
    )

