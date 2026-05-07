import cv2
import numpy as np

# ==========================================
# VIDEO PATH
# ==========================================

VIDEO_PATH = "1A-b/Test_videos/arena_video_10.mp4"

# ==========================================
# OPEN VIDEO
# ==========================================

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():

    print("Error opening video")
    exit()

# ==========================================
# GREEN HSV RANGE
# ==========================================

lower_green = np.array([40, 80, 80])
upper_green = np.array([85, 255, 255])

# ==========================================
# FRAME DIMENSIONS
# ==========================================

WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ==========================================
# HIT COUNTS
# ==========================================

top_hits = 0
bottom_hits = 0

left_hits = 0
right_hits = 0

# ==========================================
# COLLISION FLAGS
# ==========================================

top_collision = False
bottom_collision = False

left_collision = False
right_collision = False

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
    # HSV CONVERSION
    # ==========================================

    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    # ==========================================
    # GREEN MASK
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

    if len(contours) > 0:

        largest_contour = max(
            contours,
            key=cv2.contourArea
        )

        area = cv2.contourArea(largest_contour)

        if area > 500:

            # ==========================================
            # DRAW CONTOUR
            # ==========================================

            cv2.drawContours(
                frame,
                [largest_contour],
                -1,
                (255, 255, 255),
                3
            )

            # ==========================================
            # BOUNDING BOX
            # ==========================================

            x, y, w, h = cv2.boundingRect(
                largest_contour
            )

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

            # ==========================================
            # CENTROID
            # ==========================================

            M = cv2.moments(largest_contour)

            if M["m00"] != 0:

                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Draw centroid
                cv2.circle(
                    frame,
                    (cx, cy),
                    5,
                    (0, 0, 255),
                    -1
                )

                # ==========================================
                # COLLISION DETECTION
                # ==========================================

                # LEFT WALL
                if cx <= wall_threshold:

                    if not left_collision:

                        left_hits += 1
                        left_collision = True

                else:

                    left_collision = False

                # RIGHT WALL
                if cx >= WIDTH - wall_threshold:

                    if not right_collision:

                        right_hits += 1
                        right_collision = True

                else:

                    right_collision = False

                # TOP WALL
                if cy <= wall_threshold:

                    if not top_collision:

                        top_hits += 1
                        top_collision = True

                else:

                    top_collision = False

                # BOTTOM WALL
                if cy >= HEIGHT - wall_threshold:

                    if not bottom_collision:

                        bottom_hits += 1
                        bottom_collision = True

                else:

                    bottom_collision = False

    # ==========================================
    # DISPLAY COUNTS
    # ==========================================

    cv2.putText(
        frame,
        f"TOP: {top_hits}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"BOTTOM: {bottom_hits}",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"LEFT: {left_hits}",
        (30, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"RIGHT: {right_hits}",
        (30, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    # ==========================================
    # SHOW FRAME
    # ==========================================

    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(20)

    if key == 27:
        break

# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n========== FINAL COUNT ==========\n")

print("Top Hits    :", top_hits)
print("Bottom Hits :", bottom_hits)

print("Left Hits   :", left_hits)
print("Right Hits  :", right_hits)

# ==========================================
# CLEANUP
# ==========================================

cap.release()

cv2.destroyAllWindows()

