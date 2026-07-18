#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray

from bot_control.ik import inverse_kinematics


class TraceSpiral(Node):

    def __init__(self):

        super().__init__("trace_spiral")

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

        # Define your Spiral Parameters
        self.a=0.0
        self.b=0.1
        self.t=0.0

    def odom_callback(self, msg):

        # ==========================================
        # TODO:
        #
        # Update:
        #   self.x
        #   self.y
        #   self.theta
        #
        # from the received odometry message.
        #
        # ==========================================
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
        # Generate the desired point on an
        # Archimedean Spiral.
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
        rad=self.a + (self.b*self.t)
        x_target=rad*math.cos(self.t)
        y_target=rad*math.sin(self.t)

        x_error=x_target-self.x
        y_error=y_target-self.y

        vx=x_error*2.5
        vy=y_error*2.5

        w=1.5*(0.0-self.theta)

        wheel_angular_vel=inverse_kinematics(vx,vy,w)
        msg = Float64MultiArray()
        msg.data=wheel_angular_vel
        self.publisher.publish(msg)
        


def main(args=None):

    rclpy.init(args=args)

    node = TraceSpiral()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()