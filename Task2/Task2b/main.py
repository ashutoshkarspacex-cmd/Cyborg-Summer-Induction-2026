#!/usr/bin/env python3

import cv2
import numpy as np
import os

from script2b import map_arena

# ==========================================
# MAIN DRIVER FILE FOR TASK 2B
# ==========================================

def main():

    print(
        "Running Task 2B Bird's-Eye Navigator...\n"
    )

    # ==========================================
    # RUN STUDENT FUNCTION
    # ==========================================

    try:

        result = map_arena()

    except Exception as e:

        print(f"Error executing script: {e}")

        return

    # ==========================================
    # PRINT OUTPUT
    # ==========================================

    print(
        "========== DETECTED OUTPUT ==========\n"
    )

    if not result:

        print("No output returned.")

    else:

        for key, value in result.items():

            print(f"{key} : {value}")

    print(
        "\n=====================================\n"
    )

    # ==========================================
    # BASE DIRECTORY
    # ==========================================

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    # ==========================================
    # LOAD ORIGINAL IMAGE
    # ==========================================

    image_path = os.path.join(

        BASE_DIR,
        "test_images",
        "angled_arena.png"

    )

    image = cv2.imread(image_path)

    if image is None:

        print("Error loading image.")

        return

    # ==========================================
    # COPY FOR DISPLAY
    # ==========================================

    original_display = image.copy()

    # ==========================================
    # DRAW DETECTED CORNERS
    # ==========================================

    if "corner_points_detected" in result:

        colors = [

            (0, 0, 255),     # Red
            (0, 255, 0),     # Green
            (255, 0, 0),     # Blue
            (0, 255, 255)    # Yellow

        ]

        labels = [

            "TL",
            "TR",
            "BR",
            "BL"

        ]

        for i, point in enumerate(

            result["corner_points_detected"]

        ):

            x, y = point

            cv2.circle(

                original_display,
                (x, y),
                8,
                colors[i],
                -1

            )

            cv2.putText(

                original_display,

                labels[i],

                (x + 10, y),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.7,

                colors[i],

                2

            )

    # ==========================================
    # GENERATE BIRD'S-EYE VIEW
    # ==========================================

    if len(result["corner_points_detected"]) == 4:

        src_pts = np.array(

            result["corner_points_detected"],
            dtype=np.float32

        )

        dst_pts = np.array([

            [0, 0],
            [499, 0],
            [499, 499],
            [0, 499]

        ], dtype=np.float32)

        # ==========================================
        # HOMOGRAPHY MATRIX
        # ==========================================

        matrix = cv2.getPerspectiveTransform(

            src_pts,
            dst_pts

        )

        # ==========================================
        # WARP IMAGE
        # ==========================================

        warped = cv2.warpPerspective(

            image,
            matrix,
            (500, 500)

        )

        # ==========================================
        # DRAW ROBOT LOCATION
        # ==========================================

        if "robot_pixel_coord" in result:

            rx, ry = result["robot_pixel_coord"]

            cv2.circle(

                warped,
                (rx, ry),
                8,
                (0, 0, 255),
                -1

            )

            cv2.putText(

                warped,

                "Robot",

                (rx + 10, ry),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.7,

                (0, 0, 255),

                2

            )

        # ==========================================
        # DISPLAY REAL-WORLD COORDS
        # ==========================================

        if "robot_real_world_coord" in result:

            real_x, real_y = result[
                "robot_real_world_coord"
            ]

            cv2.putText(

                warped,

                f"({real_x} cm, {real_y} cm)",

                (220, 270),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.8,

                (255, 0, 0),

                2

            )

        # ==========================================
        # SAVE BIRDVIEW IMAGE
        # ==========================================

        output_path = os.path.join(

            BASE_DIR,
            "birdview.png"

        )

        cv2.imwrite(

            output_path,
            warped

        )

        print(

            f"Bird's-eye image saved at:\n"
            f"{output_path}"

        )

        # ==========================================
        # DISPLAY WINDOWS
        # ==========================================

        cv2.imshow(

            "Original Arena",
            original_display

        )

        cv2.imshow(

            "Bird's-Eye View",
            warped

        )

    else:

        cv2.imshow(

            "Original Arena",
            original_display

        )

    # ==========================================
    # WAIT AND CLOSE
    # ==========================================

    cv2.waitKey(0)

    cv2.destroyAllWindows()

# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    main()

