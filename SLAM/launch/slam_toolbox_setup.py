from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            output='screen',
            parameters=['../config/slam_toolbox_params.yaml'],
        ),
        Node(
      	    package='tf2_ros',
      	    executable='static_transform_publisher',
      	    arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser'],
      	    output='screen'
      	)
	#Node(
      	 #   package='tf2_ros',
      	 #   executable='static_transform_publisher',
      	 #   arguments=['5', '5', '0', '0', '0', '0', 'camera_link', 'base_link'],
      	  #  output='screen'
      #	)
    ])

