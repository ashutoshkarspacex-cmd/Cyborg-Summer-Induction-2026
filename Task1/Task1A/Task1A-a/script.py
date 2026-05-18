#!/usr/bin/env python3

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
        img_h = image.shape[0]
    arena_size = 8  # Fallback default
    
    # Test which grid layout successfully lands on the Start & Goal landmarks
    for size in [6, 8, 10, 12]:
        test_size = img_h // size
        found_start = False
        found_goal = False
        
        for i in range(size):
            for j in range(size):
                y1, y2 = int(i*test_size + test_size*0.3), int(i*test_size + test_size*0.7)
                x1, x2 = int(j*test_size + test_size*0.3), int(j*test_size + test_size*0.7)
                test_patch = cv2.cvtColor(image[y1:y2, x1:x2], cv2.COLOR_BGR2HSV)
                
                vibrant = (test_patch[:,:,1] >= 80) & (test_patch[:,:,2] >= 80)
                min_p = test_patch.shape[0] * test_patch.shape[1] * 0.15
                
                if np.sum(vibrant & (test_patch[:,:,0] >= 21) & (test_patch[:,:,0] <= 35)) > min_p:
                    found_start = True
                if np.sum(vibrant & (test_patch[:,:,0] >= 85) & (test_patch[:,:,0] <= 100)) > min_p:
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
        center_patch = cell[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.7)]
        hsv_cell = cv2.cvtColor(center_patch, cv2.COLOR_BGR2HSV) 
        
        row_coord = arena_size - i 
        cell_label = f"{chr(65+j)}{row_coord}"
        
        H = hsv_cell[:, :, 0]
        S = hsv_cell[:, :, 1]
        V = hsv_cell[:, :, 2]
        
        # Ignores white background, black background, and black text lines
        vibrant = (S >= 80) & (V >= 80)
        min_pixels = hsv_cell.shape[0] * hsv_cell.shape[1] * 0.15  # 15% area threshold
        
        # Clean, non-overlapping color boundaries
        if np.sum(vibrant & ((H >= 0) & (H <= 9) | (H >= 170))) > min_pixels:
            result["special_cells"][cell_label] = "DANGER"
            
        elif np.sum(vibrant & (H >= 10) & (H <= 20)) > min_pixels:
            result["special_cells"][cell_label] = "SLOW"
            
        elif np.sum(vibrant & (H >= 21) & (H <= 35)) > min_pixels:
            result["start"] = cell_label
            
        elif np.sum(vibrant & (H >= 45) & (H <= 75)) > min_pixels:
            result["special_cells"][cell_label] = "SAFE"
            
        elif np.sum(vibrant & (H >= 85) & (H <= 100)) > min_pixels:
            result["goal"] = cell_label
            
        elif np.sum(vibrant & (H >= 101) & (H <= 135)) > min_pixels:
            result["special_cells"][cell_label] = "REFUEL"

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