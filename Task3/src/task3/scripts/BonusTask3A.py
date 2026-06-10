#!/usr/bin/env python3

#Write your implementation
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
class Task3A1(Node):

    def __init__(self):

        super().__init__('spiral_tracker')
        self.cmv_vel_pub_=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.5, self.set_velocity) 
        self.get_logger().info('Draw Spiral node has been started....')
        self.counter=0.0
    def set_velocity(self):
           msg=Twist()
           msg.linear.x=1.5
           msg.angular.z=1.5*math.sin(self.counter)
           self.cmv_vel_pub_.publish(msg)
           self.counter+=0.5
        
def main(args=None):
    rclpy.init(args=args)
    node=Task3A1()
    rclpy.spin(node)
    rclpy.shutdown()