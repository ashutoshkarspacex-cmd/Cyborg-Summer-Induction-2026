#!/usr/bin/env python3

#Write your implementation
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Task3A1(Node):

    def __init__(self):

        super().__init__('spiral_tracker')
        self.cmv_vel_pub_=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.5, self.set_velocity) 
        self.get_logger().info('Draw Spiral node has been started....')
        self.linear_vel=0.0
        self.total_time=12.0
        self.counter=0.0
    def set_velocity(self):
           msg=Twist()
           if self.counter <= self.total_time:
            msg.linear.x = self.linear_vel
            msg.angular.z =  2.5
            self.cmv_vel_pub_.publish(msg)
            self.linear_vel += 0.5
            self.counter += 0.5
           else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.cmv_vel_pub_.publish(msg)
            self.get_logger().info('Completed one full spiral loop successfully. Stopping.')
            self.destroy_timer(self.set_velocity)
           
def main(args=None):
    rclpy.init(args=args)
    node=Task3A1()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()    