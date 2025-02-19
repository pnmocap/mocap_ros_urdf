# Quick start guide

本系统通过解析 Noitom Axis Studio 动捕数据，实现对人形机器人的实时控制与遥操作，支持 ROS1 和 ROS2 环境。系统包含三个核心模块，提供从数据解析到机器人驱动的完整解决方案。

如果你是第一次接触动捕设备或ROS，下面的一些概念需要了解一下：

- 动捕设备：是一种可以捕捉人体运动的设备，Noitom公司的动捕设备是Perception Neuron Studio和Perception Neuron3 Pro系列产品。
- Axis Studio：是Noitom公司提供专业的动捕软件，它跟动捕设备进行通信，并提供可以用来录制、编辑、播放、传输动捕数据。
- BVH：是一种常用的动捕数据格式，它是一种人体骨骼动作数据格式，可以用来描述人体的骨骼动作。
- URDF：是一种常用的机器人描述语言，它是一种用来描述机器人模型的语言，可以用来描述机器人各个部件的形状、尺寸、关节等信息。
- ROS：是Robot Operating System，它是一个开源的机器人操作系统，可以用来驱动机器人，并提供通信、消息传递等功能。
- ROS1：是ROS的第一个版本，它是ROS的主要版本，目前ROS2已经成为主流版本。
- ROS2：是ROS的第二个版本，它是ROS的最新版本，它提供了更加灵活的通信机制，可以用来驱动机器人。

> 注意：诺亦腾除了Axis Studio软件，还提供PNLink（有线动捕产品）的上位机软件以及Alice（光学动捕产品）的上位机软件。这些软件均可以用来获取动捕数据，并对接ROS平台。为了方便演示，本工程只使用Axis Studio软件。

## 前提

- 一台Windows PC，已安装的Axis Studio软件
- 一台Linux PC，已安装ROS1或ROS2环境

## 技术说明

- **数据流**：Axis Studio 导出 BVH → 解析关节角度 → 发布 `/joint_states` → URDF 模型驱动
- **兼容性**：C++ 版本，Python 版本
- **扩展性**：可通过修改 retarget.json 适配不同机器人模型

## 系统构成

### mocap_ros_py

**功能**：python 实现的动捕数据 ROS Publisher节点，解析BVH 数据并发布 ROS 关节控制指令。

**源码**：

~~~
https://github.com/pnmocap/mocap_ros_py.git
~~~

### mocap_ros_cpp

**功能**：C++   实现的动捕数据 ROS Publisher节点，解析BVH 数据并发布 ROS 关节控制指令。

**源码**:

~~~
https://github.com/pnmocap/mocap_ros_cpp.git
~~~

### mocap_ros_urdf

**功能**：基于 URDF 的机器人模型定义，包含机械结构、关节约束与可视化配置。

**源码**：

```
https://github.com/pnmocap/mocap_ros_urdf.git
```



以下是关于 **mocap_ros_urdf** 项目的配置和启动 ROS RViz 的简介。

# 如何配置和启动 ROS RViz

## 声明：

-  这里的ROS URDF演示模型使用的是unitree h1 Description 。

## 前提： 

- 确保已安装并配置好 ROS 环境

## 注意事项：

- 确保 Axis Studio 与 ROS 环境时间同步
- RViz 中需启用 `RobotModel` 和 `TF` 插件
- 首次运行前执行 `rosdep install` 安装缺失依赖

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

 

