#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class InfinityPathTracer(Node):
    def __init__(self):
        super().__init__('infinity_path_tracer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_period = 0.1  
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.t = 0.0
        self.get_logger().info('Infinity Path Tracer Node has been started.')

    def timer_callback(self):
        msg = Twist()
        if self.t <= 2 * math.pi:  
            msg.linear.x = 1.6  
            msg.angular.z = 2.2 * math.cos(self.t)
            self.publisher_.publish(msg)
           
            self.t += self.timer_period
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            
            self.get_logger().info('Completed one full infinity loop successfully. Stopping.')
    
            self.timer.destroy()
            

def main(args=None):
    rclpy.init(args=args)
    node = InfinityPathTracer()
   
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


        
