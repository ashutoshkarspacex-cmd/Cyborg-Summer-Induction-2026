## URDF

The robot model is defined for the `mini_bot.urdf.xacro` file.

```xml
<?xml version="1.0" ?>
<!-- 
*****************************************************************************************
*
*        =============================================
*                  Cyborg ROS Task-2
*        =============================================
*
*
*  Filename:            mini_bot.urdf.xacro
*  Created:            	11-09-2023 (by:Srivenkateshwar(e-yantra team))
*  Last Modified:       04-07-2024
*  Modified by:         SOumitra Naik   
*  
*****************************************************************************************
-->

<robot name="mini_bot" xmlns:xacro="http://www.ros.org/wiki/xacro">
    <xacro:include filename="$(find mini_bot)/urdf/materials.xacro"/>
    
    <link name ="footprint_link">

    </link>

    <joint name="footprint_joint" type="fixed">
         <origin
                xyz="0.0 0.0 0.0"
                rpy="0 0 1.047" />
        <parent link="footprint_link"/>
        <child link="base_link"/>
    </joint>

    <!--Base link-->
    <link name ="base_link">
        <inertial>
            <origin xyz="0 0.0 0.28" rpy="0 0 0" />
            <mass value="0.28" />
            <inertia
                ixx="0.011666666666667"
                ixy="0"
                ixz="0"
                iyy="0.011666666666667"
                iyz="0"
                izz="0.011666666666667" />
        </inertial>

        <collision name="collision">
            <origin
                xyz="0 0.0 0.28"
                rpy="0 0 0" />
            <geometry>
                <mesh filename ="file://$(find mini_bot)/meshes/bot_1.dae"
                      scale="0.01 0.01 0.01"/>
            </geometry>
        </collision>

        <visual>
            <origin
                xyz="0 0 0.28"
                rpy="0 0 0" />
            <geometry>
                <mesh filename ="file://$(find mini_bot)/meshes/bot_1.dae"
                      scale="0.01 0.01 0.01"/>
            </geometry>
        </visual>
    </link>

    <!-- left wheel -->
    <link name ="Left_wheel">
        <inertial>
            <origin
                xyz="0.0 -0.05 0.0"
                rpy="1.57 0 0" />
            <mass value="0.060" />
            <inertia
                ixx="1.825e-4"
                ixy="0"
                ixz="0.00000000"
                iyy="1.825e-4"
                iyz="0"
                izz="1.825e-4" />
        </inertial>

        <collision name="L_collision">
            <origin
                xyz="0.0 -0.05 0.0"
                rpy="1.57 0 0" />
            <geometry>
                <cylinder length="0.13" radius="0.14"/>
            </geometry>
        </collision>

        <visual>
            <origin
                xyz="0.0 0.0 0.0"
                rpy="0.0 0.0 0.0" />
            <geometry>
                <mesh filename ="file://$(find mini_bot)/meshes/wheel.stl"
                      scale="5 5 5"/>
            </geometry>
        </visual>
    </link>

    <gazebo reference="Left_wheel">
        <material>Gazebo/Red</material>
    </gazebo>

    <!-- right_wheel -->
    <link name ="Right_wheel">
        <inertial>
            <origin
                xyz="0.0 -0.05 0.0"
                rpy="-1.57 0.0 0.0"/>
            <mass value="0.060" />
            <inertia
                ixx="1.825e-4"
                ixy="0"
                ixz="0.00000000"
                iyy="1.825e-4"
                iyz="0"
                izz="1.825e-4" />
        </inertial>

        <collision name="R_collision">
            <origin
                xyz="0.0 -0.05 0.0"
                rpy="-1.57 0.0 0.0" />
            <geometry>
                <cylinder length="0.13" radius="0.14"/>
            </geometry>
        </collision>

        <visual>
            <origin
                xyz="0.0 0.0 0.0"
                rpy="0 0 0.0" />
            <geometry>
                <mesh filename ="file://$(find mini_bot)/meshes/wheel.stl"
                      scale="5 5 5"/>
            </geometry>
        </visual>
    </link>

    <gazebo reference="Right_wheel">
        <material>Gazebo/Blue</material>
    </gazebo>

    <!-- joints -->

    <!-- Right wheel joint -->
    <joint name ="Right_wheel_joint" type="continuous">
        <origin
            xyz="0.58 -0.36 0.18"
            rpy="0.0 0.0 -2.12" />
        <parent link="base_link"/>
        <child link="Right_wheel"/>
        <axis xyz="0.0 1.0 0.0"/>
        <limit effort="5" velocity="5" />
    </joint>

    <!-- Left wheel Joint -->
    <joint name ="Left_wheel_joint" type="continuous">
        <origin
            xyz="0.0 0.68 0.18"
            rpy="0 0 0" />
        <parent link="base_link"/>
        <child link="Left_wheel"/>
        <axis xyz="0.0 1.0 0.0"/>
        <limit effort="5" velocity="5" />
    </joint>
<!--
plugins
-->


</robot>
```
## PLUGIN

```xml
<!-- after defining the robot description add the following under robot tag only-->
<gazebo>
<plugin
    filename="libignition-gazebo-diff-drive-system.so"
    name="ignition::gazebo::systems::DiffDrive">

    <left_joint>Left_wheel_joint</left_joint>
    <right_joint>Right_wheel_joint</right_joint>

    <wheel_separation>1.19</wheel_separation> 
    <wheel_radius>0.14</wheel_radius>

    <odom_publish_frequency>1</odom_publish_frequency>

    <topic>cmd_vel</topic>

</plugin>
</gazebo>
```

## SDF or world File

```xml

<?xml version="1.0" ?>
<sdf version="1.8">

  <world name="diff_drive_world">

    <!-- Physics -->
    <physics name="1ms" type="ignored">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>

    <!-- Essential Gazebo systems -->
    <plugin
      filename="libignition-gazebo-physics-system.so"
      name="ignition::gazebo::systems::Physics">
    </plugin>

    <plugin
      filename="libignition-gazebo-user-commands-system.so"
      name="ignition::gazebo::systems::UserCommands">
    </plugin>

    <plugin
      filename="libignition-gazebo-scene-broadcaster-system.so"
      name="ignition::gazebo::systems::SceneBroadcaster">
    </plugin>

    <!-- Sun -->
    <light type="directional" name="sun">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>

      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>

      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>

      <direction>-0.5 0.1 -0.9</direction>
    </light>

    <!-- Ground Plane -->
    <model name="ground_plane">
      <static>true</static>

      <link name="link">

        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
            </plane>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>

          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>

      </link>
    </model>

    <!-- Robot -->

    <include>
      <uri>model://mini_bot</uri>
      <pose>0 0 0 0 0 0</pose>
    </include>

  </world>

</sdf>
```
