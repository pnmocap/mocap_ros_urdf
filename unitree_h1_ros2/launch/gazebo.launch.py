import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # get gazebo_ros package path
    gazebo_ros_share_dir = get_package_share_directory('gazebo_ros')
    h1_description_share_dir = get_package_share_directory('h1_description')

    # parameters
    paused_arg = DeclareLaunchArgument(
        'paused',
        default_value='true',
        description='Whether to start the simulation paused'
    )

    # empty_world.launch.py in Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_share_dir, 'launch', 'empty_world.launch.py')
        ),
        launch_arguments={
            'paused': LaunchConfiguration('paused')
        }.items()
    )

    # launch spawn_model node
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_model',
        arguments=[
            '-file', os.path.join(h1_description_share_dir, 'urdf', 'h1.urdf'),
            '-urdf',
            '-z', '1.05',
            '-model', 'h1_description'
        ],
        output='screen'
    )

    return LaunchDescription([
        paused_arg,
        gazebo_launch,
        spawn_model_node
    ])