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

        ####################################################
        ## TODO 2
        ##
        ## Check whether all goals
        ## have been reached.
        ##
        ####################################################

        ####################################################
        ## TODO 3
        ##
        ## Obtain the current goal
        ## coordinates.
        ##
        ####################################################

        ####################################################
        ## TODO 4
        ##
        ## Compute position error
        ##
        ## ex
        ## ey
        ##
        ####################################################

        ####################################################
        ## TODO 5
        ##
        ## Compute Euclidean distance
        ## from the current goal.
        ##
        ####################################################

        ####################################################
        ## TODO 6
        ##
        ## If distance is less than
        ## goal_threshold,
        ##
        ## move to next goal.
        ##
        ####################################################

        ####################################################
        ## TODO 7
        ##
        ## Compute desired robot
        ## velocity using a
        ## proportional controller.
        ##
        ####################################################

        ####################################################
        ## TODO 8
        ##
        ## Convert world frame velocity
        ## into robot frame velocity.
        ##
        ####################################################

        ####################################################
        ## TODO 9
        ##
        ## Limit the robot velocity.
        ##
        ####################################################

        ####################################################
        ## TODO 10
        ##
        ## Use inverse_kinematics()
        ## to compute wheel velocities.
        ##
        ####################################################

        ####################################################
        ## TODO 11
        ##
        ## Publish wheel velocities
        ## to
        ##
        ## /wheel_velocity_controller/commands
        ##
        ####################################################

        pass


############################################################


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