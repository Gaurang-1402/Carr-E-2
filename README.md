# Carr-E-2
🚃Autonomous luggage cart


## Running the robot on RVIZ

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
source setup.bash
```

Now, open a new terminal and run the robot state publisher

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







