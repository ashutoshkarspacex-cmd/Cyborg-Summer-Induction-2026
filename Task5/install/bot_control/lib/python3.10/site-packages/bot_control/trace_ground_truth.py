#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from tf2_msgs.msg import TFMessage

import matplotlib.pyplot as plt


class TracePath(Node):

    def __init__(self):

        super().__init__("trace_path")

        self.path_x = []
        self.path_y = []

        self.create_subscription(
            TFMessage,
            "/world/default/pose/info",
            self.callback,
            10,
        )

    def callback(self, msg):

        for tf in msg.transforms:

            if tf.child_frame_id == "mini_bot":

                self.path_x.append(
                    tf.transform.translation.x
                )

                self.path_y.append(
                    tf.transform.translation.y
                )

    def plot(self):

        if len(self.path_x) == 0:
            print("No robot pose received.")
            return

        plt.figure(figsize=(6, 6))

        plt.plot(
            self.path_x,
            self.path_y,
            color="blue",
            linewidth=2,
        )

        plt.scatter(
            self.path_x[0],
            self.path_y[0],
            color="green",
            s=100,
            label="Start",
        )

        plt.scatter(
            self.path_x[-1],
            self.path_y[-1],
            color="red",
            s=100,
            label="End",
        )

        plt.xlabel("X (m)")
        plt.ylabel("Y (m)")
        plt.title("Trajectory from Gazebo Ground Truth")
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