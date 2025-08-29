from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('vihang_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'vihang.urdf.xacro')
    
    return LaunchDescription([
        Node(
            package = 'robot_state_publisher',
            executable = 'robot_state_publisher',
            name = 'robot_state_publisher',
            output = 'screen',
            parameters = [{'use_sim_time': False}],
            arguments = [urdf_file]
        ),
        
        Node(
            package = 'joint_state_publisher',
            executable = 'joint_state_publisher',
            name = 'joint_state_publisher',
            output = 'screen'
        ),
        
        Node(
            package = 'rviz2',
            executable = 'rviz2',
            name = 'rviz2',
            output = 'screen'   
        ),
    ])