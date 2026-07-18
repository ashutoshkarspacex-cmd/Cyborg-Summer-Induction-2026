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

        pass

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

        pass


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