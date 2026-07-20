#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry

import matplotlib.pyplot as plt


class TracePath(Node):

    def __init__(self):

        super().__init__("trace_path")

        self.path_x = []
        self.path_y = []

        self.create_subscription(
            Odometry,
            "/odom",
            self.callback,
            10,
        )

    def callback(self, msg):

        self.path_x.append(
            msg.pose.pose.position.x
        )

        self.path_y.append(
            msg.pose.pose.position.y
        )

    def plot(self):

        if len(self.path_x) == 0:
            print("No odometry received.")
            return

        plt.figure(figsize=(6, 6))

        plt.plot(
            self.path_x,
            self.path_y,
            linewidth=2,
            color="blue"
        )

        plt.scatter(
            self.path_x[0],
            self.path_y[0],
            color="green",
            s=100,
            label="Start"
        )

        plt.scatter(
            self.path_x[-1],
            self.path_y[-1],
            color="red",
            s=100,
            label="End"
        )

        plt.xlabel("X (m)")
        plt.ylabel("Y (m)")
        plt.title("Trajectory from Odometry")
        plt.grid(True)
        plt.axis("equal")
        plt.legend()

        plt.show()


def main(args=None):

    rclpy.init(args=args)

    node = TracePath()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.plot()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()