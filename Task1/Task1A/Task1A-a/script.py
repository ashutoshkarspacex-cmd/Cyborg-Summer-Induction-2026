#!/usr/bin/env python3
import cv2
import numpy as np


def analyze_arena(input_image):

    # ==========================================
    # LOAD IMAGE
    # ==========================================

    image = cv2.imread(input_image)

    if image is None:

        print("Error loading image.")
        return {}

    # ==========================================
    # INITIALIZE OUTPUT
    # ==========================================

    result = {

        "arena_size": None,
        "start": None,
        "goal": None,
        "special_cells": {}

    }

    # ==========================================
    # WRITE YOUR LOGIC BELOW
    # ==========================================

    '''
    Steps you may follow:

    1. Detect arena size
    2. Divide arena into grid cells
    3. Convert image to HSV 
    4. Detect START cell
    5. Detect GOAL cell
    6. Detect special colored cells
    7. Map cells to arena coordinates
    8. Store outputs in result dictionary

    Color Meaning
    Red : Danger Zone
    Green : Safe Zone
    Blue : Refuel Station
    Orange : Slow Terrain
    Yellow : Start Position
    Cyan : Goal Position
    '''
    # Example:

    # result["arena_size"] = 8
    # result["start"] = "A1"
    # result["goal"] = "H8"

    # result["special_cells"]["B2"] = "DANGER"
    # result["special_cells"]["D5"] = "SAFE"
    arena_size = image.shape[0]
    result["arena_size"] = arena_size

    # divide arena into grid cells
    for i in range(arena_size):
        for j in range(arena_size):
            cell = image[i*arena_size:(i+1)*arena_size, j*arena_size:(j+1)*arena_size]
            # convert cell to HSV
            hsv_cell = cv2.cvtColor(cell, cv2.COLOR_BGR2HSV)
            # detect start cell
            if np.any((hsv_cell[:, :, 0] >= 15) & (hsv_cell[:, :, 0] <= 35) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["start"] = f"{chr(65+j)}{i+1}"
            # detect goal cell
            if np.any((hsv_cell[:, :, 0] >= 85) & (hsv_cell[:, :, 0] <= 100) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["goal"] = f"{chr(65+j)}{i+1}"
            # detect special cells
            if np.any((hsv_cell[:, :, 0] >= 0) & (hsv_cell[:, :, 0] <= 10) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["special_cells"][f"{chr(65+j)}{i+1}"] = "DANGER"
            elif np.any((hsv_cell[:, :, 0] >= 50) & (hsv_cell[:, :, 0] <= 70) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["special_cells"][f"{chr(65+j)}{i+1}"] = "SAFE"
            elif np.any((hsv_cell[:, :, 0] >= 100) & (hsv_cell[:, :, 0] <= 130) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["special_cells"][f"{chr(65+j)}{i+1}"] = "REFUEL"
            elif np.any((hsv_cell[:, :, 0] >= 10) & (hsv_cell[:, :, 0] <= 20) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
                result["special_cells"][f"{chr(65+j)}{i+1}"] = "SLOW"

    # ==========================================
    # SORT SPECIAL CELLS
    # ==========================================

    sorted_cells = dict(

        sorted(

            result["special_cells"].items(),

            key=lambda item: (

                item[0][0],
                int(item[0][1:])

            )
        )
    )

    result["special_cells"] = sorted_cells

    # ==========================================
    # RETURN FINAL OUTPUT
    # ==========================================
    return result