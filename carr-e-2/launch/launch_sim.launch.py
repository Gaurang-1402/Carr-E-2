import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

# the purpose of this script is to replace running 3 separate terminals 
# (to run robot_state_publisher, gazebo_launch, and gazebo_spawn)
#  with 1 terminal where this script calls all 3 launch commands

def generate_launch_description():

    package_name = 'carr-e-2'

    # include our own rsp.launch.py    
    package_directory = get_package_share_directory(package_name)
    filepath = os.path.join(package_directory, 'launch', 'rsp.launch.py')
    # force use_sim_true to be true
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([filepath]), 
        launch_arguments={'use_sim_time': 'True'}.items()
    )


    # in order to make gazebo and rviz synchronize better in terms of fps, we pass extra params to
    # gazebo (set clock to 400hz from gazebo_params.yaml)
    gazebo_params_file = os.path.join(package_directory, 'config', 'gazebo_params.yaml')


    # include gazebo launch file from gazebo_ros package
    gazebo_package_directory = get_package_share_directory('gazebo_ros')
    gazebo_filepath = os.path.join(gazebo_package_directory, 'launch', 'gazebo.launch.py')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_filepath]),
        launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
    )

    # run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you have a single robot in the simulation
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py', arguments=['-topic', 'robot_description', '-entity', 'carr-e-2'], output='screen')

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["diff_cont"]
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_broad"]

    )

    # launch robot_state_publisher, gazebo, and spawn node so you don't need 3 separate terminals
    return LaunchDescription([
        robot_state_publisher, 
        gazebo, 
        spawn_entity,
        diff_drive_spawner,
        joint_broad_spawner
    ])
