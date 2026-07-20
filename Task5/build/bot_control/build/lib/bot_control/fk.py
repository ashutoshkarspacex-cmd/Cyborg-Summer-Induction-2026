#!/usr/bin/env python3

import math as np


def forward_kinematics(omega_left, omega_right, omega_rear):

    #write your implementation here
    wheel_radius=0.14
    distance_in_plane=0.68

    left_wheel=0.0
    right_wheel=-2.12
    rear_wheel=2.12
    
    vx=(2/3)*wheel_radius*(-omega_left*np.sin(left_wheel)-omega_rear*np.sin(rear_wheel)+omega_right*np.sin(right_wheel))
    vy=(2/3)*wheel_radius*(-omega_left*np.cos(left_wheel)-omega_rear*np.cos(rear_wheel)+omega_right*np.cos(right_wheel))

    omega_avg=(wheel_radius/(3*distance_in_plane))*(omega_rear+omega_left+omega_right)
    return vx,vy,omega_avg


def main():

    wl = float(input("Left wheel (rad/s): "))
    wr = float(input("Right wheel (rad/s): "))
    wb = float(input("Rear wheel (rad/s): "))
    

    vx, vy, omega = forward_kinematics(
        wl,
        wr,
        wb
    )

    print(f"\nvx     : {vx:.3f} m/s")
    print(f"vy     : {vy:.3f} m/s")
    print(f"omega  : {omega:.3f} rad/s")


if __name__ == "__main__":
    main()