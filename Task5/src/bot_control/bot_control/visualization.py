#!/usr/bin/env python3

import math
import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from geometry_msgs.msg import Pose2D
from cv_bridge import CvBridge

from rclpy.qos import qos_profile_sensor_data


class Visualization(Node):

    def __init__(self):

        super().__init__("visualization")

        self.bridge = CvBridge()

        self.frame = None

        self.robot_x = None
        self.robot_y = None
        self.robot_theta = 0.0

        self.path = []

        self.pose_received = False
        self.pose_warning_printed = False

        self.create_subscription(
            Image,
            "/camera",
            self.image_callback,
            qos_profile_sensor_data
        )

        self.create_subscription(
            Pose2D,
            "/bot_pose",
            self.pose_callback,
            10
        )

    #######################################################

    def image_callback(self, msg):

        try:

            # Don't force the encoding
            self.frame = self.bridge.imgmsg_to_cv2(msg)

            self.update_display()

        except Exception as e:

            self.get_logger().error(f"Image Conversion Error : {e}")

    #######################################################

    def pose_callback(self, msg):

        if not self.pose_received:

            self.get_logger().info(
                "Pose2D topic detected. Started trajectory visualization."
            )

        self.pose_received = True

        self.robot_x = int(msg.x)
        self.robot_y = int(msg.y)
        self.robot_theta = msg.theta

        self.path.append((self.robot_x, self.robot_y))

    #######################################################

    def update_display(self):

        if self.frame is None:
            return

        display = self.frame.copy()

        if not self.pose_received:

            if not self.pose_warning_printed:

                self.get_logger().info(
                    "Waiting for Pose2D messages on /bot_pose..."
                )

                self.pose_warning_printed = True

        else:

            # Draw Path
            for i in range(1, len(self.path)):

                cv2.line(
                    display,
                    self.path[i - 1],
                    self.path[i],
                    (0, 255, 0),
                    2
                )

            # Draw Robot
            cv2.circle(
                display,
                (self.robot_x, self.robot_y),
                6,
                (0, 0, 255),
                -1
            )

            # Draw Heading
            end_x = int(
                self.robot_x +
                40 * math.cos(self.robot_theta)
            )

            end_y = int(
                self.robot_y +
                40 * math.sin(self.robot_theta)
            )

            cv2.arrowedLine(
                display,
                (self.robot_x, self.robot_y),
                (end_x, end_y),
                (255, 0, 0),
                2
            )

        cv2.imshow("Arena Visualization", display)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):

            self.path.clear()

            self.get_logger().info("Trajectory Cleared.")

        elif key == ord('q'):

            rclpy.shutdown()


###########################################################

def main(args=None):

    rclpy.init(args=args)

    node = Visualization()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    cv2.destroyAllWindows()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()