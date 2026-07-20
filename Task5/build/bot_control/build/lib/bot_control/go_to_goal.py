#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Float64MultiArray

from bot_control.ik import inverse_kinematics


class GoToGoal(Node):

    def __init__(self):

        super().__init__("go_to_goal")

        ####################################################
        ## Subscriber
        ####################################################

        self.create_subscription(
            Pose2D,
            "/bot_pose",
            self.pose_callback,
            10
        )

        ####################################################
        ## Publisher
        ####################################################

        self.cmd_pub = self.create_publisher(
            Float64MultiArray,
            "/wheel_velocity_controller/commands",
            10
        )

        ####################################################
        ## Robot Pose
        ####################################################

        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_theta = 0.0

        ####################################################
        ## Goal Points
        ##
        ## Copy the corner marker coordinates
        ## obtained in Task 5C.
        ####################################################

        self.goal_points = [
            # (x1,y1),
            # (x2,y2),
            # (x3,y3),
            # (x4,y4)
        ]

        self.current_goal = 0

        ####################################################
        ## Controller Parameters
        ####################################################

        self.kp = 0.002

        self.goal_threshold = 20

        self.max_velocity = 0.4

        ####################################################

        self.get_logger().info(
            "Go To Goal Node Started."
        )

    ########################################################

    def pose_callback(self, msg):

        ####################################################
        ## TODO 1
        ##
        ## Update robot pose using
        ## Pose2D message.
        ##
        ####################################################
        msg=Pose2D()
        msg.x=self.robot_x
        msg.y=self.robot_y
        msg.theta=self.robot_theta
        ####################################################
        ## TODO 2
        ##
        ## Check whether all goals
        ## have been reached.
        ##
        ####################################################
        if self.current_goal==4:
            self.get_logger().info('All goals have been reached')
            return
        else:
            current_goal=self.goal_points[self.current_goal]
            target_x, target_y = current_goal[0], current_goal[1]
            
            ex=target_x-self.robot_x
            ey=target_y-self.robot_y
            
            euclidean_distance=(ex**2 + ey**2)**0.5
            if euclidean_distance<=self.goal_threshold:
                self.current_goal+=1
                
            vx=self.kp*ex
            vy=self.kp*ey    
            cos_h=math.cos(self.robot_theta)
            sin_h=math.sin(self.robot_theta)
            
            vx_robot =  vx* cos_h + vy * sin_h
            vy_robot = -vx * sin_h + vy * cos_h
            
            omega=self.kp*(0.0-self.robot_theta)
            
            robot_vel=(vx_robot**2 + vy_robot**2)**0.5
            
            if robot_vel>=self.max_velocity:
                vx_robot*=(self.max_velocity/robot_vel)
                vy_robot*=(self.max_velocity/robot_vel)
            
            wheel_angular_vel=inverse_kinematics(vx_robot,vy_robot,omega)
            msg1=Float64MultiArray()
            msg1.data=wheel_angular_vel
            self.cmd_pub.publish(msg1)
 
def main(args=None):

    rclpy.init(args=args)

    node = GoToGoal()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()