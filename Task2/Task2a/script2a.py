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
    col=9
    row=6
    square_size=2.5
    objp = np.zeros((row*col, 3), np.float32)
    objp[:,:2]=np.mgrid[0:col,0:row].T.reshape(-1,2)*square_size
    gray_shape = None
    # TODO: Use glob to read all images from the 'calibration_images' folder
    objpoints=[]
    imgpoints=[]
    images=glob.glob('calibration_images/*.png')
    
    # TODO: Loop through the images, convert to grayscale, and use cv2.findChessboardCorners()
    for img in images:
        img=cv2.imread(img)
        if img is None:
            continue
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,corners=cv2.findChessboardCorners(gray,(col,row),None)
        if ret== True:
            objpoints.append(objp)
            imgpoints.append(corners)
            gray_shape=gray.shape[::1]

    # TODO: Use cv2.calibrateCamera() to calculate the camera matrix (mtx) and distortion coefficients (dist)
    if gray_shape is None:
        print("Error: Calibration failed. No checkerboard images processed.")
        return result
    ret,mtx,dist,rvecs,tvecs=cv2.calibrateCamera(objpoints,imgpoints,gray_shape,None,None)

    # TODO: Calculate the trace of the camera matrix (sum of the main diagonal elements)
    trace_value=np.trace(mtx)
    result["camera_matrix_trace"] = round(trace_value, 2)


    # ==========================================
    # STEP 2: Image Undistortion
    # ==========================================
    # TODO: Read the target image 'test_images/test_arena.png'
    target_img=cv2.imread('test_images/test_arena.jpg')
    if target_img is None:
        print("Error: Could not read the target image.")
        return result
    
    # TODO: Use cv2.undistort() with your calculated mtx and dist to fix the image
    fix_img=cv2.undistort(target_img,mtx,dist,None,mtx)


    # ==========================================
    # STEP 3: ArUco Detection & Pose Estimation
    # ==========================================
    # TODO: Initialize the ArUco detector for DICT_4X4_50
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    
    # TODO: Detect markers in the UNDISTORTED image
    corners, ids, rejected = detector.detectMarkers(fix_img)
    
    # TODO: For each detected marker, use cv2.solvePnP() to estimate its pose
    # Hint: You need the real-world 3D coordinates of the marker corners (Marker size is 5.0 cm)
    marker_size=5.0
    marker_3d_points=np.array([[-marker_size/2, marker_size/2, 0],
                                [marker_size/2, marker_size/2, 0],
                                [marker_size/2, -marker_size/2, 0],
                                [-marker_size/2, -marker_size/2, 0]], dtype=np.float32)
    
    if ids is not None:
        for i in range(len(ids)):
            marker_id = int(ids[i][0])
            marker_corners = corners[i][0]
    success, rvec, tvec = cv2.solvePnP(marker_3d_points, marker_corners, mtx,dist)
    # TODO: Extract the z-distance and x-offset from the translation vector (tvec)
    if success:
        x_offset=round(tvec[0][0], 1)
        z_distance=round(tvec[2][0], 1)
        
        result["markers"][f"id_{marker_id}"] = {"distance_z": z_distance, "x_offset": x_offset} 

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