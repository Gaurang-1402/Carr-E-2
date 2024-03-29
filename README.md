# Carr-E-2

🚃 Autonomous luggage cart

## Basic setup

If stuck with weird errors, run the basic setup again and then attempt the same process.

First, create a folder called dev_ws and clone this repository



```
mkdir dev_ws
cd dev_ws
git clone https://github.com/Gaurang-1402/Carr-E-2
```


Now you have to build your ws with colcon



```
colcon build --symlink-install
```
Adding `--symlink-install` makes it so that you don't have to rebuild every time you change urdfs but instead only have to build again if a new urdf file is added.

Now, you have to source the setup.bash file


```
source install/setup.bash
```


## Running the robot on RVIZ

Open a new terminal and run the robot state publisher

```
ros2 launch carr-e-2 rsp.launch.py
```

If everything works well, open a new terminal and run rviz using the configuration created by Gaurang
```
rviz2 -d carr-e-2/config/carr-e-2-rviz-config.rviz 
```

The wheels need to get continous values. Since this is a simulation we need to provide these values through a joint state publisher gui. Open a new terminal and run

```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```


## Running the robot on Gazebo

Install Gazebo if not done already

```
sudo apt install ros-foxy-gazebo-ros-pkgs
```

Open a new terminal and run the robot state publisher

```
ros2 launch carr-e-2 rsp.launch.py use_sim_time:=true
```
We need to provide the ```use_sim_time:=true``` param to make the robot state publisher follow the simulation's time.

You can verify this by running
```
ros2 param get /robot_state_publisher use_sim_time 
$ Boolean value is: True
```

We need to run RVIZ before we run Gazebo so run rviz by using the following command

```
rviz2 -d carr-e-2/config/carr-e-2-gazebo-lidar-config.rviz 
```


Ensure basic setup is rerun. Now to run Gazebo, open a new terminal and run 


```
ros2 launch carr-e-2 launch_sim.launch.py world:=./carr-e-2/worlds/obstacles.world
```

A gazebo window will open with the robot correctly placed.

We use a world called "obstacles.world" created by Gaurang by default. But this can be changed.


We can now use teleop to control the movement of the robot by opening a new terminal and running the following command

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

We can now control the movement of the robot using keys on the keyboard

## Camera plugins

Install the following packages

```
sudo apt install ros-foxy-image-transport-plugins
sudo apt install ros-foxy-rqt-image-view
```

On a new terminal run 

```
ros2 run rqt_image_view rqt_image_view
```

We need to run RVIZ before we run Gazebo so run rviz by using the following command

```
rviz2 -d carr-e-2/config/carr-e-2-gazebo-camera-config.rviz 
```

## ROS2 Control

Install the following packages

```
sudo apt install ros-foxy-ros2-control ros-foxy-ros2-controllers ros-foxy-gazebo-ros2-control
```

Then run these 2 commands

```

ros2 run controller_manager spawner.py diff_cont

ros2 run controller_manager spawner.py joint_broad
```

Finally run the following command to control the robot using the keyboard

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```

## Joystick control in Gazebo

Open a new terminal and run

```
ros2 run joy_tester test_joy
```

This will help you debug any errors if present. Along with test_joy run this on a new terminal

```
ros2 topic echo joy
```

Run the joystick node

```
ros2 launch carr-e-2 joystick.launch.py
```


To check cmd_vel, run

```
ros2 topic echo /diff_cont/cmd_vel_unstamped

```

## Run SLAM toolbox

Install packages

```
sudo apt install ros-foxy-slam-toolbox
```

Then run

```
ros2 launch slam_toolbox online_async_launch.py params_file:=./carr-e-2/config/mapper_params_online_async.yaml use_sim_time:=true
```

## Run Nav2

Install packages

```
sudo apt install ros-foxy-navigation2 ros-foxy-nav2-bringup ros-foxy-turtlebot3*
```

On 2 different terminals, run map server

```
ros2 run nav2_util lifecycle_bringup map_server
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=my_map_save.yaml -p use_sim_time:=true
```

Running AMCL

```
ros2 run nav2_util lifecycle_bringup amcl
ros2 run nav2_amcl amcl --ros-args -p use_sim_time:=true
```

TWIST COMMAND

```
ros2 run twist_mux twist_mux --ros-args --params-file ./carr-e-2/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped
```


SECOND THING

```
ros2 launch nav2_bringup navigation_launch.py my_map:=./my_map_save.yaml  use_sim_time:=true
```


# Physical robot

## Testing motors

```
miniterm -e /dev/ttyUSB0 57600
```
```
 ros2 run serial_motor_demo driver --ros-args -p serial_port:=/dev/ttyUSB0 -p baud_rate:=57600 -p loop_rate:=30 -p encoder_cpr:=678
```

## Testing Lidar

Install rplidar 

```
sudo apt install ros-foxy-rplidar-ros
```
Run rplidar node
```
ros2 run rplidar_ros rplidar_composition --ros-args -p serial_port:=/dev/ttyUSB0  -p frame_id:=laser_frame -p  angle_compensate:=true -p scan_mode:=Standard 
```
Stop or start motor

```
 ros2 service call /stop_motor std_srvs/srv/Empty {}

 ros2 service call /start_motor std_srvs/srv/Empty {}
```

## Camera

```
sudo apt install libraspberrypi-bin v4l-utils ros-foxy-v4l2-camera

```

```
ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]" -p camera_frame_id:=camera_link_optical

```


