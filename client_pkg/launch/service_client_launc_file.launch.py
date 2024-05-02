from launch import LaunchDescription
from launch_ros.actions import Node

def generate_Launch_Description():
    return LaunchDescription([
        Node(
            package='client_pkg',
            executable='service_client',
            output='screen',
        )
    ])