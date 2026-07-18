#!/usr/bin/env python3

import math
import cv2
import cv2.aruco as aruco

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from geometry_msgs.msg import Pose2D

from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data


class Feedback(Node):

    def __init__(self):

        super().__init__("feedback")

        ####################################################
        ## OpenCV Bridge
        ####################################################

        self.bridge = CvBridge()

        ####################################################
        ## Subscriber
        ####################################################

        self.create_subscription(
            Image,
            "/camera",
            self.image_callback,
            qos_profile_sensor_data
        )

        ####################################################
        ## Publisher
        ####################################################

        self.pose_pub = self.create_publisher(
            Pose2D,
            "/bot_pose",
            10
        )

        ####################################################
        ## ArUco Detector
        ####################################################

        self.dictionary = aruco.getPredefinedDictionary(
            aruco.DICT_4X4_100
        )

        self.parameters = aruco.DetectorParameters()

        self.detector = aruco.ArucoDetector(
            self.dictionary,
            self.parameters
        )

        ####################################################
        ## Robot Marker ID
        ####################################################

        self.robot_id = 4

        ####################################################
        ## Data Containers
        ####################################################

        # Robot Pose

        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_theta = 0.0

        # Corner Marker Centres

        self.corner_markers = {}

        ####################################################

        self.get_logger().info(
            "Feedback Node Started"
        )

    ########################################################

    def image_callback(self, msg):

        ####################################################
        ## TODO 1
        ##
        ## Convert ROS Image to OpenCV Image.
        ##
        ####################################################

        ####################################################
        ## TODO 2
        ##
        ## Detect all ArUco markers.
        ##
        ####################################################

        ####################################################
        ## TODO 3
        ##
        ## Draw detected markers.
        ##
        ####################################################

        ####################################################
        ## TODO 4
        ##
        ## Loop through all detected markers.
        ##
        ####################################################

        ####################################################
        ## TODO 5
        ##
        ## Compute the centre of every marker.
        ##
        ####################################################

        ####################################################
        ## TODO 6
        ##
        ## Compute the orientation (theta)
        ## of every detected marker.
        ##
        ####################################################

        ####################################################
        ## TODO 7
        ##
        ## Store the centre coordinates of
        ## corner markers (IDs 0,1,2,3)
        ## inside self.corner_markers.
        ##
        ####################################################

        ####################################################
        ## TODO 8
        ##
        ## If the detected marker is the
        ## robot marker, update
        ##
        ## self.robot_x
        ## self.robot_y
        ## self.robot_theta
        ##
        ####################################################

        ####################################################
        ## TODO 9
        ##
        ## Publish the robot pose on
        ## /bot_pose using Pose2D.
        ##
        ####################################################

        ####################################################
        ## TODO 10
        ##
        ## Display the image with
        ## detected markers.
        ##
        ####################################################

        pass


############################################################


def main(args=None):

    rclpy.init(args=args)

    node = Feedback()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    cv2.destroyAllWindows()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()