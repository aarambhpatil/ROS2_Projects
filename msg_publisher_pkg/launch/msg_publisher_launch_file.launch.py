from launch import LaunchDescription
from launch_ros.actions import Node

def generate_Launch_Description():
    return LaunchDescription([
        Node(
            package="msg_publisher",
            executable="msg_publisher_node",
            output="screen"
        )
    ])