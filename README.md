# Carr-E-2
🚃Autonomous luggage cart

# Basic setup

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
Adding ```--symlink-install ``` makes it so that you don't have to rebuild every time you change urdfs but instead only have to build again if a new urdf file is added

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

Ensure all windows are closed and the basic setup is rerun. Open a new terminal and run

```
ros2 launch carr-e-2 launch_sim.launch.py
```

A gazebo window will open with the robot correctly plaxed

We can now use teleop to control the movement of the robot by running the following command

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

We can now control the movement of the robot using keys on the keyboard


