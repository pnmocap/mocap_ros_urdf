import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 获取 ros_gz_sim 包路径
    ros_gz_sim_share_dir = get_package_share_directory('ros_gz_sim')
    unitree_h1_ros2_share_dir = get_package_share_directory('unitree_h1_ros2')

    # 参数
    paused_arg = DeclareLaunchArgument(
        'paused',
        default_value='false',
        description='Whether to start the simulation paused'
    )

    # 启动 Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_share_dir, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # 启动 spawn_model 节点
    spawn_model_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_model',
        arguments=[
            '-file', os.path.join(unitree_h1_ros2_share_dir, 'urdf', 'h1.urdf'),
            '-urdf',
            '-z', '1.05',
            '-model', 'unitree_h1_ros2'
        ],
        output='screen'
    )

    return LaunchDescription([
        paused_arg,
        gazebo_launch,
        spawn_model_node
    ])