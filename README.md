# ydlidar_x4_pro_ros

This is YDLidar X4 Pro package for ROS2

# Prerequisites

This package depends on [ydlidar_ros2_driver](https://github.com/YDLIDAR/ydlidar_ros2_driver) so if you don't have it or out of date, do it first.

# How to build package

1.Create your workspace with a ```src``` sub-directory.

2.Inside a ```src``` ,clone this git with ```git clone https://github.com/Dr2546/ydlidar_x4_pro_ros.git``` and paste ```lidar``` and ```lidar_interfaces``` under ```src```.

3.In the root of your workspace,run ```rosdep install -i --from-path src --rosdistro foxy -y``` to check dependencies.

> Note:Ros distro may vary depends on you,this project use Ros2 foxy.

4.Run ```colcon build``` or ```colcon build --packages-select lidar lidar_interfaces``` if your workspace has many packages and you only want to build this package.

5.In your root workspace , go inside  ```install/lidar/lib```. If there is no ```lidar``` directory, create it,then copy ```lidar.py``` ```lidarcli.py``` from ```install/lidar/bin``` and paste under ```lidar```.

6.In your root workspace , go inside  ```install/lidar/share/lidar```. If there is no ```launch``` directory, create it,then copy ```lidar_launch.py```  from ```src/lidar/launch``` and paste under ```launch```.

# How to use/run package
1.Open up your workspace in 2 terminal.

2.Run ```. install/setup.bash``` in both terminals.

3.First terminal run ```ros2 launch lidar lidar_launch.py```.

4.Second terminal ,when you want to get lidar informations, run ```ros2 run lidar lidarcli getpos```.

## About lidar_interfaces

lidar_interfaces has 2 msg and 1 srv.

`msg: PolarCoordinate (float32 deg,float32 range)`

`msg: Position (PolarCoordinate[] ranges)`

`srv: GetPos (string req --- Position ranges)`
