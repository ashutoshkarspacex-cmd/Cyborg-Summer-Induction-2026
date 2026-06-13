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
        window = 11.0
        c = window / 2.0
        rad_max = 4.5
        self.linear_vel = 0.5
        self.angular_vel = 1.0
        theta_max= rad_max / self.linear_vel
        self.counter=0.0
    def set_velocity(self):
           msg=Twist()
           self.linear_vel += 0.01

           msg.linear.x = self.linear_vel
           msg.angular.z = self.angular_vel
           self.cmv_vel_pub_.publish(msg)
           
def main(args=None):
    rclpy.init(args=args)
    node=Task3A1()
    rclpy.spin(node)
    rclpy.shutdown()