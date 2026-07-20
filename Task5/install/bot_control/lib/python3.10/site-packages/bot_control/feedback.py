#!/usr/bin/env python3

import numpy as np
import cv2
import cv2.aruco as aruco
import math

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
        self.bridge = CvBridge()

        self.get_logger().info(
            "Feedback Node Started"
        )

    ########################################################

    def image_callback(self,msg):

        ####################################################
        ## TODO 1
        ##
        ## Convert ROS Image to OpenCV Image.
        ##
        ####################################################
     try:
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
     except:
        print("Conversion failure")
        return

  
     corners, ids, rejected = self.detector.detectMarkers(cv_image)
     print(ids)

     if ids is not None:
            cv2.aruco.drawDetectedMarkers(cv_image, corners, ids)

            for i in range(len(ids)):
                marker_id = ids[i][0]
                marker_corners = corners[i][0] 
                center_x = float(np.mean(marker_corners[:, 0]))
                center_y = float(np.mean(marker_corners[:, 1]))
                top_edge_x = (marker_corners[0][0] + marker_corners[1][0]) / 2.0
                top_edge_y = (marker_corners[0][1] + marker_corners[1][1]) / 2.0
                
                theta = math.atan2(-(top_edge_y - center_y), top_edge_x - center_x)

                if marker_id in [0,1,2,3]:
                 self.corner_markers[marker_id]=[center_x,center_y]
                 
                if marker_id==self.robot_id:
                    self.robot_x=center_x
                    self.robot_y=center_y
                    self.robot_theta=theta 
                    
                    
            if len(self.corner_markers) == 4:
             self.get_logger().info("\nALL 4 CORNER MARKERS DETECTED")
             for marker_id in sorted(self.corner_markers.keys()):
                  coords = self.corner_markers[marker_id]
                  self.get_logger().info(f"Marker ID {marker_id}: Center X = {coords[0]:.2f}, Center Y = {coords[1]:.2f}")        
            if self.robot_id in ids:
                pose_msg=Pose2D()
                pose_msg.x = self.robot_x
                pose_msg.y = self.robot_y
                pose_msg.theta = self.robot_theta
                self.pose_pub.publish(pose_msg)
                
     cv2.imshow("Aruco detection arena",cv_image)
     cv2.waitKey(1)



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