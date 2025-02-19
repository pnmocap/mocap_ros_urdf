



# 启动ROS Visualizer

这里的ROS URDF模型使用的是unitree h1 Description 。

## ROS1

1. 创建工作空间（仅第一次）

```
mkdir -p ~/catkin_noitom/src
cd ~/catkin_noitom/src
catkin_init_workspace
cp -r  unitree_h1_ros1  ~/catkin_noitom/src/
```

2. 编译并运行ROS1 RVIZ

```
cd  ~/catkin_noitom
catkin_make
source  devel/setup.bash
roslaunch unitree_h1_ros1 display.launch
```

## ROS2

1. 创建工作空间（仅第一次）

```
mkdir -p ~/catkin_noitom
cp -r unitree_h1_ros2  ~/catkin_noitom
```

2. 编译并运行ROS2 RVIZ

```
cd  ~/catkin_noitom/unitree_h1_ros2
colcon build
source  install/setup.bash
ros2 launch  unitree_h1_ros2 display.launch.py
```

 

