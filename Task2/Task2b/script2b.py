import cv2
import numpy as np

def map_arena():
    """
    Task 2B: Perspective Transformation and Coordinate Mapping
    """
    # Initialize the output dictionary
    result = {
        "corner_points_detected": [],
        "robot_pixel_coord": [],
        "robot_real_world_coord": []
    }

    # ==========================================
    # STEP 1: Corner Detection (Color Tracking)
    # ==========================================
    # TODO: Read the target image 'test_images/angled_arena.png'
    
    # TODO: Convert the image to HSV color space
    
    # TODO: Create HSV masks to isolate the Red, Green, Blue, and Yellow corners
    
    # TODO: Find contours for each mask and calculate the centroid (cx, cy) using moments (M["m10"] / M["m00"])
    
    # TODO: Store the coordinates in the exact order: [Top-Left(Red), Top-Right(Green), Bottom-Right(Blue), Bottom-Left(Yellow)]
    # result["corner_points_detected"] = [[cx_r, cy_r], [cx_g, cy_g], [cx_b, cy_b], [cx_y, cy_y]]


    # ==========================================
    # STEP 2: Perspective Transformation
    # ==========================================
    # TODO: Define your source points as a float32 numpy array (the 4 centroids calculated above)
    
    # TODO: Define your destination points as a flat 500x500 pixel square
    # Example: [[0,0], [500,0], [500,500], [0,500]]
    
    # TODO: Use cv2.getPerspectiveTransform() to calculate the 3x3 Homography Matrix
    
    # TODO: Apply cv2.warpPerspective() to flatten the angled arena into a 500x500 top-down view


    # ==========================================
    # STEP 3: Robot Detection on Warped Arena
    # ==========================================
    # TODO: On the NEW warped 500x500 image, initialize an ArUco detector (DICT_4X4_50)
    
    # TODO: Detect the marker representing the robot (ID 1)
    
    # TODO: Calculate the center pixel coordinates (cx, cy) of the detected marker
    # result["robot_pixel_coord"] = [cx, cy]


    # ==========================================
    # STEP 4: Real-World Coordinate Conversion
    # ==========================================
    # Context: The 500x500 pixel warped image represents a physical arena of 200cm x 200cm.
    # The top-left corner is the origin [0.0, 0.0] cm.
    
    # TODO: Use linear scaling to convert the robot's pixel coordinates to real-world centimeters.
    # result["robot_real_world_coord"] = [x_cm, y_cm]


    return result

if __name__ == "__main__":
    # Test your function
    output = map_arena()
    print("Task 2B Output:")
    print(output)