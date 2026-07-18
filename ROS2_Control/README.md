# ROS 2 Control Reference Package

## Purpose

This directory is provided **only as a reference** to help you understand the integration of the **ROS 2 Control** framework with a mobile robot.

The reference package demonstrates how to configure:

* ROS 2 Control plugins
* `<ros2_control>` tags in the URDF
* Controller configuration using YAML files
* Gazebo ROS 2 Control plugin
* ROS–Gazebo bridge
* Launch files for loading and managing controllers

---

## Important Notice

**Do not use this package directly for the mini task.**

You are expected to integrate **ROS 2 Control** into **your own line-following robot** developed in the previous task. Reusing the robot model, URDF, or package provided here for the submission is **not allowed**.
---

## Commonly Used ROS 2 Controllers

| Controller                                                  | Typical Application                    | Message Type                                                  | Default Command Topic                                | Example CLI Command                                                                                                                       |
| ----------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `diff_drive_controller/DiffDriveController`                 | Differential drive mobile robots       | `geometry_msgs/msg/Twist`                                     | `/cmd_vel`                                           | `ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.3}, angular: {z: 0.5}}" -r 10`                                           |
| `ackermann_steering_controller/AckermannSteeringController` | Ackermann steering vehicles            | `geometry_msgs/msg/Twist` or `geometry_msgs/msg/TwistStamped` | `/ackermann_steering_controller/reference_unstamped` | `ros2 topic pub /ackermann_steering_controller/reference_unstamped geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.3}}" -r 10` |
| `forward_position_controller/ForwardCommandController`      | Position control of one or more joints | `std_msgs/msg/Float64MultiArray`                              | `/forward_position_controller/commands`              | `ros2 topic pub /forward_position_controller/commands std_msgs/msg/Float64MultiArray "{data: [1.57, 0.0]}" -r 10`                         |
| `forward_velocity_controller/ForwardCommandController`      | Direct wheel/joint velocity control    | `std_msgs/msg/Float64MultiArray`                              | `/forward_velocity_controller/commands`              | `ros2 topic pub /forward_velocity_controller/commands std_msgs/msg/Float64MultiArray "{data: [5.0, 8.0]}" -r 10`                          |
| `joint_trajectory_controller/JointTrajectoryController`     | Robotic arms and manipulators          | `trajectory_msgs/msg/JointTrajectory`                         | `/joint_trajectory_controller/joint_trajectory`      | Publish a `trajectory_msgs/msg/JointTrajectory` message containing joint names, positions, and timing information.                        |

---

## Expected Outcome

After studying this reference package, you should be able to:

* Integrate ROS 2 Control into your own robot.
* Configure different controllers according to the robot's application.
* Load and switch controllers using the `controller_manager`.
* Develop ROS 2 nodes to command different controllers.
* Understand how changing the controller changes the robot's command interface while keeping the same robot hardware description.

Your final implementation should be based on **your own line-following robot**, while using this package only as a guide for understanding the ROS 2 Control workflow.
