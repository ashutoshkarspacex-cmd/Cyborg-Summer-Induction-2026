#!/usr/bin/env python3

#Write your implementation
from turtle import distance

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import math
class Task3B(Node):
    def __init__(self):
        super().__init__('turtle_pose_tracker')
        self.cmv_vel_pub_=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.get_logger().info('Turtle Pose Tracker Node has been started....')
        self.target_points = [
            [5.5, 9.5],
            [7.0, 5.5],
            [10.0, 5.5],
            [7.8, 3.0],
            [9.0, 0.5],
            [5.5, 2.5],[2.0, 0.5],
             [3.2, 3.0],
              [1.0, 5.5],
                [4.0, 5.5],
   ]
        self.current_pose=None
        self.current_target_index=0

    def pose_callback(self, msg):
        self.current_pose=msg
        if self.current_target_index < len(self.target_points):
            i=self.current_target_index
            target_x, target_y = self.target_points[i]
            
            distance_error = math.sqrt((target_x - self.current_pose.x) ** 2 + (target_y - self.current_pose.y) ** 2)
            if distance_error<0.05:
                self.get_logger().info(f'Reached target point {i+1} at ({target_x}, {target_y}).')
                self.current_target_index += 1
            msg=Twist()
            msg.linear.x=distance_error*2
            self.get_logger().info(f"current distance from target point {i+1} is {distance_error:.2f}")
            desired_angle=math.atan2(target_y-self.current_pose.y,target_x-self.current_pose.x)
            angle_diff=desired_angle-self.current_pose.theta 
            heading_error= math.atan2(math.sin(angle_diff), math.cos(angle_diff))
            msg.angular.z=heading_error*4
            self.get_logger().info(f"current heading error from target point {i+1} is {heading_error:.2f}")
            self.cmv_vel_pub_.publish(msg)

            



def main(args=None):
    rclpy.init(args=args)
    node=Task3B()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()




