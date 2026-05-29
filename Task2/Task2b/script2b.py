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
    img=cv2.imread('test_images/angled_arena.png')
    
    # TODO: Convert the image to HSV color space
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # TODO: Create HSV masks to isolate the Red, Green, Blue, and Yellow corners
    red_mask=cv2.inRange(hsv,(0,100,100),(10,255,255))
    red_mask2=cv2.inRange(hsv,(160,100,100),(180,255,255))
    green_mask=cv2.inRange(hsv,(50,100,100),(70,255,255))
    blue_mask=cv2.inRange(hsv,(110,100,100),(130,255,255))
    yellow_mask=cv2.inRange(hsv,(20,100,100),(30,255,255))
    
    # TODO: Find contours for each mask and calculate the centroid (cx, cy) using moments (M["m10"] / M["m00"])
    contours, _ = cv2.findContours(red_mask+red_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M=cv2.moments(contour)
        if M["m00"]!=0:
            cx_r=int(M["m10"]/M["m00"])
            cy_r=int(M["m01"]/M["m00"])
            result["corner_points_detected"].append([cx_r, cy_r])
    contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M=cv2.moments(contour)
        if M["m00"]!=0:
            cx_g=int(M["m10"]/M["m00"])
            cy_g=int(M["m01"]/M["m00"])
            result["corner_points_detected"].append([cx_g, cy_g])
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours: 
        M=cv2.moments(contour)
        if M["m00"]!=0:
            cx_b=int(M["m10"]/M["m00"])
            cy_b=int(M["m01"]/M["m00"])
            result["corner_points_detected"].append([cx_b, cy_b])
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M=cv2.moments(contour)
        if M["m00"]!=0:
            cx_y=int(M["m10"]/M["m00"])
            cy_y=int(M["m01"]/M["m00"])
            result["corner_points_detected"].append([cx_y, cy_y])
    
    # TODO: Store the coordinates in the exact order: [Top-Left(Red), Top-Right(Green), Bottom-Right(Blue), Bottom-Left(Yellow)]
    result["corner_points_detected"] = [[cx_r, cy_r], [cx_g, cy_g], [cx_b, cy_b], [cx_y, cy_y]]


    # ==========================================
    # STEP 2: Perspective Transformation
    # ==========================================
    # TODO: Define your source points as a float32 numpy array (the 4 centroids calculated above)
    source_points=np.array([[cx_r, cy_r], [cx_g, cy_g], [cx_b, cy_b], [cx_y, cy_y]], dtype=np.float32)
    
    # TODO: Define your destination points as a flat 500x500 pixel square
    # Example: [[0,0], [500,0], [500,500], [0,500]]
    destination_points=np.array([[0,0],[500,0],[500,500],[0,500]], dtype=np.float32)
    # TODO: Use cv2.getPerspectiveTransform() to calculate the 3x3 Homography Matrix
    matrix = cv2.getPerspectiveTransform(source_points, destination_points)
    # TODO: Apply cv2.warpPerspective() to flatten the angled arena into a 500x500 top-down view
    flat_image = cv2.warpPerspective(hsv, matrix, (500, 500))

    # ==========================================
    # STEP 3: Robot Detection on Warped Arena
    # ==========================================
    # TODO: On the NEW warped 500x500 image, initialize an ArUco detector (DICT_4X4_50)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    
    # TODO: Detect the marker representing the robot (ID 1)

    # TODO: Calculate the center pixel coordinates (cx, cy) of the detected marker
    
    corners, ids, rejected = detector.detectMarkers(flat_image)
    if ids is not None and 1 in ids:
        index=np.where(ids==1)[0][0]
        robot_corners=corners[index][0]
        center=np.mean(robot_corners,axis=0)
        cx=int(center[0])
        cy=int(center[1])
        result["robot_pixel_coord"] = [cx, cy]

    


    # ==========================================
    # STEP 4: Real-World Coordinate Conversion
    # ==========================================
    # Context: The 500x500 pixel warped image represents a physical arena of 200cm x 200cm.
    # The top-left corner is the origin [0.0, 0.0] cm.
    
    # TODO: Use linear scaling to convert the robot's pixel coordinates to real-world centimeters.
    real_size=200.0  # cm
    pixel_size=500.0 # pixels
    scale=real_size/pixel_size
    x_cm=cx*scale
    y_cm=cy*scale
    result["robot_real_world_coord"] = [x_cm, y_cm]


    return result

if __name__ == "__main__":
    # Test your function
    output = map_arena()
    print("Task 2B Output:")
    print(output)