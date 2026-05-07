import cv2
import numpy as np


def analyze_video(video_path):

    # ==========================================
    # OUTPUT DICTIONARY
    # ==========================================

    result = {

        "top_wall_hits": 0,
        "bottom_wall_hits": 0,
        "left_wall_hits": 0,
        "right_wall_hits": 0

    }

    # ==========================================
    # OPEN VIDEO
    # ==========================================

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():

        print("Error opening video")
        return result

    # ==========================================
    # GREEN COLOR RANGE (HSV)
    # ==========================================

    # Students may modify/tune these values

    lower_green = np.array([40, 80, 80])
    upper_green = np.array([85, 255, 255])

    # ==========================================
    # FRAME DIMENSIONS
    # ==========================================

    WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # ==========================================
    # COLLISION FLAGS
    # ==========================================

    left_collision = False
    right_collision = False

    top_collision = False
    bottom_collision = False

    # ==========================================
    # WALL THRESHOLD
    # ==========================================

    wall_threshold = 50

    # ==========================================
    # PROCESS VIDEO
    # ==========================================

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # ==========================================
        # CONVERT FRAME TO HSV
        # ==========================================

        hsv = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2HSV
        )

        # ==========================================
        # CREATE GREEN MASK
        # ==========================================

        mask = cv2.inRange(
            hsv,
            lower_green,
            upper_green
        )

        # ==========================================
        # FIND CONTOURS
        # ==========================================

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # ==========================================
        # WRITE YOUR LOGIC BELOW
        # ==========================================

        '''
        Suggested Steps:

        1. Find the largest contour
        2. Ignore very small contours
        3. Compute contour centroid
        4. Detect wall collisions
        5. Count:
           - top wall hits
           - bottom wall hits
           - left wall hits
           - right wall hits

        '''

        # ==========================================
        # HINT FOR WALL DETECTION
        # ==========================================

        '''
        Example:

        if cx <= wall_threshold:
            # Left wall touched

        if cx >= WIDTH - wall_threshold:
            # Right wall touched

        if cy <= wall_threshold:
            # Top wall touched

        if cy >= HEIGHT - wall_threshold:
            # Bottom wall touched
        '''

    # ==========================================
    # RELEASE VIDEO
    # ==========================================

    cap.release()

    return result

