import cv2
import numpy as np
import glob

def localize_bot():
    """
    Task 2A: Camera Calibration and ArUco Pose Estimation
    """
    # Initialize the output dictionary with exact keys required by the evaluator
    result = {
        "camera_matrix_trace": 0.0,
        "markers": {}
    }

    # ==========================================
    # STEP 1: Camera Calibration
    # ==========================================
    # TODO: Define the real-world 3D coordinates for the checkerboard corners (9x6 grid, 2.5cm square size)
    
    # TODO: Use glob to read all images from the 'calibration_images' folder
    
    # TODO: Loop through the images, convert to grayscale, and use cv2.findChessboardCorners()
    
    # TODO: Use cv2.calibrateCamera() to calculate the camera matrix (mtx) and distortion coefficients (dist)
    
    # TODO: Calculate the trace of the camera matrix (sum of the main diagonal elements)
    # result["camera_matrix_trace"] = round(trace_value, 2)


    # ==========================================
    # STEP 2: Image Undistortion
    # ==========================================
    # TODO: Read the target image 'test_images/test_arena.png'
    
    # TODO: Use cv2.undistort() with your calculated mtx and dist to fix the image


    # ==========================================
    # STEP 3: ArUco Detection & Pose Estimation
    # ==========================================
    # TODO: Initialize the ArUco detector for DICT_4X4_50
    
    # TODO: Detect markers in the UNDISTORTED image
    
    # TODO: For each detected marker, use cv2.solvePnP() to estimate its pose
    # Hint: You need the real-world 3D coordinates of the marker corners (Marker size is 5.0 cm)
    
    # TODO: Extract the z-distance and x-offset from the translation vector (tvec)
    # Populate the result dictionary in the format: result["markers"]["id_<num>"] = {"distance_z": <val>, "x_offset": <val>}


    # ==========================================
    # SORT MARKERS BY ARUCO ID
    # ==========================================
    result["markers"] = dict(

        sorted(

            result["markers"].items(),

            key=lambda item: int(
                item[0].split("_")[1]
            ),
            reverse=True
        )

    )

    # ==========================================
    # RETURN FINAL OUTPUT
    # ==========================================

    return result

if __name__ == "__main__":
    # Test your function
    output = localize_bot()
    print("Task 2A Output:")
    print(output)