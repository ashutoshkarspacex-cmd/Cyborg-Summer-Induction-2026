#!/usr/bin/env python3
from email.mime import image
from unittest import result

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
    img_h = image.shape[0]
    arena_size = 8  # Fallback default
    for size in [6, 8, 10, 12]:
        test_cell_size = img_h // size
        found_start = False
        found_goal = False
        for i in range(size):
            for j in range(size):
                # Sample a tiny window at the center of the test cell
                cy = int((i + 0.5) * test_cell_size)
                cx = int((j + 0.5) * test_cell_size)
                pixel_hsv = cv2.cvtColor(np.uint8([[image[cy, cx]]]), cv2.COLOR_BGR2HSV)[0][0]
                h, s, v = pixel_hsv[0], pixel_hsv[1], pixel_hsv[2]
                
                if s >= 70 and v >= 70:
                    if 21 <= h <= 35:   # Yellow Start
                        found_start = True
                    if 85 <= h <= 100:  # Cyan Goal
                        found_goal = True
                        
                        
            if found_start and found_goal:
             arena_size = size
             break
    result["arena_size"] = arena_size
    cell_size = img_h // arena_size
#divide arena into cell_size
    for i in range(arena_size):
     for j in range(arena_size):
        cell = image[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
        
      
        h, w = cell.shape[:2]
        center_patch = cell[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.75)]
        hsv_cell = cv2.cvtColor(center_patch, cv2.COLOR_BGR2HSV) 
        
       
        row_coord = arena_size - i 
        cell_label = f"{chr(65+j)}{row_coord}"
        
        # Detect start cell
        if np.any((hsv_cell[:, :, 0] >= 21) & (hsv_cell[:, :, 0] <= 35) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["start"] = cell_label
            
        # Detect goal cell 
        if np.any((hsv_cell[:, :, 0] >= 85) & (hsv_cell[:, :, 0] <= 100) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["goal"] = cell_label
            
        # Detect special cells
        if np.any((hsv_cell[:, :, 0] >= 0) & (hsv_cell[:, :, 0] <= 9) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["special_cells"][cell_label] = "DANGER"
        elif np.any((hsv_cell[:, :, 0] >= 45) & (hsv_cell[:, :, 0] <= 75) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["special_cells"][cell_label] = "SAFE"
        elif np.any((hsv_cell[:, :, 0] >= 101) & (hsv_cell[:, :, 0] <= 135) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["special_cells"][cell_label] = "REFUEL"
        elif np.any((hsv_cell[:, :, 0] >= 10) & (hsv_cell[:, :, 0] <= 20) & (hsv_cell[:, :, 1] >= 100) & (hsv_cell[:, :, 2] >= 100)):
            result["special_cells"][cell_label] = "SLOW"

    # ==========================================
    # SORT SPECIAL CELLS
    # ==========================================
    # 
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