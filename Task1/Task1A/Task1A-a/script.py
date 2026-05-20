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
    
    # ==========================================
    # WRITE YOUR LOGIC BELOW
    # ==========================================
    h=image.shape[0]
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    colour_ranges = {
        "DANGER": ([0, 100, 100], [10, 255, 255]),       # Red
        "SAFE": ([50, 100, 100], [70, 255, 255]),       # Green
        "REFUEL": ([110, 100, 100], [130, 255, 255]),   # Blue
        "SLOW": ([15, 100, 100], [35, 255, 255]),       # Orange
        "START": ([20, 50, 100], [34, 255, 255]),      # Yellow
        "GOAL": ([85, 50, 100], [95, 255, 255])        # Cyan
    }
    arena_size=8

    for i in [6,8,10,12]:
        flag=False
        cell_size=h//i
        for k in range(i):
            for j in range(i):
                cx= j*cell_size+cell_size//2
                cy= k*cell_size+cell_size//2
                pixel_hsv=hsv[max(0, cy-3):min(h, cy+3), max(0, cx-3):min(h, cx+3)]
                for label in ["START","GOAL"]:
                    lower=np.array(colour_ranges[label][0])
                    upper=np.array(colour_ranges[label][1])
                    match_mask = (pixel_hsv >= lower) & (pixel_hsv <= upper)
                    if np.any(np.all(match_mask, axis=-1)):
                        arena_size=i
                        
                        flag=True
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    result["arena_size"]=arena_size
    cell_size=h//arena_size
    for k in range(arena_size):
        for j in range(arena_size):
            is_text=False
            cx= j*cell_size+cell_size//2
            cy= k*cell_size+cell_size//2
            pixel_hsv=hsv[max(0, cy-6):min(h, cy+3), max(0, cx-6):min(h, cx+3)]
            lower=np.array(colour_ranges["START"][0])
            upper=np.array(colour_ranges["START"][1])
            match_mask = (pixel_hsv >= lower) & (pixel_hsv <= upper)
            if np.any(np.all(match_mask, axis=-1)):
                result["start"]=chr(65+j)+str(arena_size-k)
                is_text=True
            lower=np.array(colour_ranges["GOAL"][0])
            upper=np.array(colour_ranges["GOAL"][1])
            match_mask = (pixel_hsv >= lower) & (pixel_hsv <= upper)
            if np.any(np.all(match_mask, axis=-1)):
                result["goal"]=chr(65+j)+str(arena_size-k)
                is_text=True


            if not is_text:
             for label in ["DANGER","SAFE","REFUEL","SLOW"]:
                pixel_hsv = hsv[cy, cx]
                h_val, s_val, v_val = pixel_hsv
            
                lower=np.array(colour_ranges[label][0])
                upper=np.array(colour_ranges[label][1])
                if np.all(pixel_hsv >= lower) and np.all(pixel_hsv <= upper):
                    cell_label=chr(65+j)+str(arena_size-k)
                    result["special_cells"][cell_label]=label
                    break
            


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