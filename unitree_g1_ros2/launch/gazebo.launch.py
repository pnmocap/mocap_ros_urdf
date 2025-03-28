import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # get ros_gz_sim package path
    ros_gz_sim_share_dir = get_package_share_directory('ros_gz_sim')
    unitree_g1_ros2_share_dir = get_package_share_directory('unitree_g1_ros2')

    # parameters
    paused_arg = DeclareLaunchArgument(
        'paused',
        default_value='false',
        description='Whether to start the simulation paused'
    )

    # empty_world.launch.py in Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_share_dir, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # launch spawn_model node
    spawn_model_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_model',
        arguments=[
            '-file', os.path.join(unitree_g1_ros2_share_dir, 'urdf', 'h1.urdf'),
            '-urdf',
            '-z', '1.05',
            '-model', 'unitree_g1_ros2'
        ],
        output='screen'
    )

    return LaunchDescription([
        paused_arg,
        gazebo_launch,
        spawn_model_node
    ])