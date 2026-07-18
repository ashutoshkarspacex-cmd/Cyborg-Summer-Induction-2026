#!/usr/bin/env python3

import math as np

def inverse_kinematics(vx, vy, omega):

    #write your implementation  here

    #TODO: Get your wheel radius and coordinates from urdf and implent your function
    wheel_radius=0.14
    distance_in_plane=0.68
    
    left_wheel=0.0
    right_wheel=-2.12
    rear_wheel=2.12

    w_left= float((1.0/distance_in_plane)*(-vx*np.sin(left_wheel)+ vy*np.cos(left_wheel)+ distance_in_plane*omega))
    w_right= float((1.0/distance_in_plane)*(-vx*np.sin(right_wheel)+ vy*np.cos(right_wheel)+ distance_in_plane*omega))
    w_rear=float((1.0/distance_in_plane)*(-vx*np.sin(rear_wheel)+ vy*np.cos(rear_wheel)+ distance_in_plane*omega))

    return w_left, w_right,w_rear

def main():

    vx = float(input("vx (m/s): "))
    vy = float(input("vy (m/s): "))
    omega = float(input("omega (rad/s): "))

    wl, wr, wb = inverse_kinematics(vx, vy, omega)

    print(f"\nLeft wheel  : {wl:.3f} rad/s")
    print(f"Right wheel : {wr:.3f} rad/s")
    print(f"Rear wheel  : {wb:.3f} rad/s")


if __name__ == "__main__":
    main()