#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray

from bot_control.ik import inverse_kinematics


class TraceEllipse(Node):

    def __init__(self):

        super().__init__("trace_ellipse")

        self.publisher = self.create_publisher(
            Float64MultiArray,
            "/wheel_velocity_controller/commands",
            10
        )

        self.create_subscription(
            Odometry,
            "/odom",
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(
            0.02,
            self.control_loop
        )

        # Current Robot Pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Ellipse Parameters

        # Define your ellipse parameters
        self.a=2.5
        self.b=1.5
        self.t=0.0


    def odom_callback(self, msg):
        self.x=msg.pose.pose.position.x
        self.y=msg.pose.pose.position.y
       
        q=msg.pose.pose.orientation

        q_list=[q.x,q.y,q.z,q.w]
        siny_cosp = 2 * (q_list[-1] * q_list[2] + q_list[0] * q_list[1])
        cosy_cosp=1-2*(q_list[1]**2 + q_list[2]**2)
        self.theta=math.atan2(siny_cosp,cosy_cosp)
        
    def control_loop(self):

        # ==========================================
        # TODO:
        #
        # Increment the trajectory parameter.
        #
        # Generate the desired point on the ellipse.
        #
        # Calculate the position error.
        #
        # Compute the required robot velocity
        # (vx, vy, omega) using the position error.
        #
        # Use inverse_kinematics() to obtain
        # wheel angular velocities.
        #
        # Publish the wheel angular velocities
        # using Float64MultiArray.
        #
        # ==========================================
        self.t+=0.02
        x_target=self.a*math.cos(self.t)
        y_target=self.b*math.sin(self.t)

        x_error=x_target-self.x
        y_error=y_target-self.y

        vx=x_error*2.0
        vy=y_error*2.0

        w=1.5*(0.0-self.theta)

        wheel_angular_vel=inverse_kinematics(vx,vy,w)
        msg = Float64MultiArray()
        msg.data=wheel_angular_vel
        self.publisher.publish(msg)

def main(args=None):

    rclpy.init(args=args)

    node = TraceEllipse()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()