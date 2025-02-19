import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

# generate_launch_description() 函数是入口点，用于生成 LaunchDescription 对象，描述了启动的节点及其参数。
# FindPackageShare 类用于查找指定包的共享目录，以便获取该包中的资源文件。在这里，它用于获取机器人描述包（roobot_description）的共享目录路径。
# LaunchDescription 对象用于存储要启动的节点及其参数。

# 其中涉及三个节点
# joint_state_publisher_gui 负责发布机器人关节数据信息，通过joint_states话题发布
# robot_state_publisher_node负责发布机器人模型信息robot_description，并将joint_states数据转换tf信息发布
# rviz2_node负责显示机器人的信息
# 最终，通过调用 ld.add_action() 将这些节点添加到 LaunchDescription 对象中，并将其返回，以便由 ROS 2 的启动系统加载并执行。
# joint_state_publisher_gui，还有一个兄弟叫做joint_state_publisher   两者区别在于joint_state_publisher_gui运行起来会跳出一个界面，通过界面可以操作URDF中能动的关节



def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('unitree_h1_ros2')  #需要修改的地方:robot_description 修改为对应的功能包名称
    launch_dir = os.path.join(bringup_dir, 'launch')

    # Launch configuration variables specific to simulation
    rviz_config_file = LaunchConfiguration('rviz_config_file')
    use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
    use_joint_state_pub = LaunchConfiguration('use_joint_state_pub')
    use_rviz = LaunchConfiguration('use_rviz')
    urdf_file= LaunchConfiguration('urdf_file')
    
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value=os.path.join(bringup_dir, 'rviz', 'rviz.rviz'), 
        description='Full path to the RVIZ config file to use')  
    declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
        'use_robot_state_pub',
        default_value='True',
        description='Whether to start the robot state publisher')
    declare_use_joint_state_pub_cmd = DeclareLaunchArgument(
        'use_joint_state_pub',
        default_value='True',
        description='Whether to start the joint state publisher')
    declare_use_rviz_cmd = DeclareLaunchArgument(
        'use_rviz',
        default_value='True',
        description='Whether to start RVIZ')

    declare_urdf_cmd = DeclareLaunchArgument(
        'urdf_file',
        default_value=os.path.join(bringup_dir, 'urdf', 'h1.urdf'),#需要修改的地方
        description='Whether to start RVIZ') 


    start_robot_state_publisher_cmd = Node(
        condition=IfCondition(use_robot_state_pub),
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        #parameters=[{'use_sim_time': use_sim_time}],
        arguments=[urdf_file])
    
    start_joint_state_publisher_cmd = Node(
        condition=IfCondition(use_joint_state_pub),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        arguments=[urdf_file])
    
    rviz_cmd = Node(
        condition=IfCondition(use_rviz),
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen')
        

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_rviz_config_file_cmd)
    ld.add_action(declare_urdf_cmd)
    ld.add_action(declare_use_robot_state_pub_cmd)
    ld.add_action(declare_use_joint_state_pub_cmd)
    ld.add_action(declare_use_rviz_cmd)


    # Add any conditioned actions
    ld.add_action(start_joint_state_publisher_cmd)
    ld.add_action(start_robot_state_publisher_cmd)
    ld.add_action(rviz_cmd)

    return ld   
