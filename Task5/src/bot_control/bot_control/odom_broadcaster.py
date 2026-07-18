#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, TransformStamped

from tf2_ros import TransformBroadcaster

from bot_control.fk import forward_kinematics


class OdomPublisher(Node):

    def __init__(self):

        super().__init__("odom_publisher")

        self.create_subscription(
            JointState,
            "/joint_states",
            self.joint_callback,
            10
        )

        self.odom_pub = self.create_publisher(
            Odometry,
            "/odom",
            10
        )

        self.tf_broadcaster = TransformBroadcaster(self)

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.last_time = self.get_clock().now()

    def joint_callback(self, msg):

        try:
            wl = msg.velocity[msg.name.index("Left_wheel_joint")]
            wr = msg.velocity[msg.name.index("Right_wheel_joint")]
            wb = msg.velocity[msg.name.index("Rear_wheel_joint")]
        except ValueError:
            return

        # ---------- Forward Kinematics ----------

        vx, vy, omega = forward_kinematics(
            wl,
            wr,
            wb
        )

        # ---------- Time ----------

        now = self.get_clock().now()

        dt = (
            now - self.last_time
        ).nanoseconds / 1e9

        self.last_time = now

        if dt <= 0.0:
            return

        # ---------- Integrate Pose ----------

        self.theta += omega * dt

        self.x += (
            vx * math.cos(self.theta)
            - vy * math.sin(self.theta)
        ) * dt

        self.y += (
            vx * math.sin(self.theta)
            + vy * math.cos(self.theta)
        ) * dt

        # ---------- Quaternion ----------

        q = Quaternion()

        q.x = 0.0
        q.y = 0.0
        q.z = math.sin(self.theta / 2.0)
        q.w = math.cos(self.theta / 2.0)

        # ---------- Publish Odometry ----------

        odom = Odometry()

        odom.header.stamp = now.to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "footprint_link"

        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0

        odom.pose.pose.orientation = q

        odom.twist.twist.linear.x = vx
        odom.twist.twist.linear.y = vy
        odom.twist.twist.angular.z = omega

        self.odom_pub.publish(odom)

        # ---------- Publish TF ----------

        tf = TransformStamped()

        tf.header.stamp = now.to_msg()
        tf.header.frame_id = "odom"
        tf.child_frame_id = "footprint_link"

        tf.transform.translation.x = self.x
        tf.transform.translation.y = self.y
        tf.transform.translation.z = 0.0

        tf.transform.rotation = q

        self.tf_broadcaster.sendTransform(tf)


def main(args=None):

    rclpy.init(args=args)

    node = OdomPublisher()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()