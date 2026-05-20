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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _, thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
    row_sums = np.sum(thresh, axis=1)
    col_sums = np.sum(thresh, axis=0)
    
    cutoff = thresh.max() * 0.3
    top    = int(np.argmax(row_sums > cutoff))
    left   = int(np.argmax(col_sums > cutoff))
    bottom = len(row_sums) - int(np.argmax(row_sums[::-1] > cutoff)) - 1
    right  = len(col_sums) - int(np.argmax(col_sums[::-1] > cutoff)) - 1
    
    ax, ay = left, top
    aw = right - left
    ah = bottom - top

    # Calibrated color profiles accommodating thin anti-aliased text lines
    colour_ranges = {
        "DANGER": [([0,   120, 80],  [10,  255, 255]),
                   ([170, 120, 80],  [180, 255, 255])],   # Red [cite: 19]
        "SAFE":   [([35,  80,  60],  [85,  255, 255])],   # Green [cite: 19]
        "REFUEL": [([100, 80,  60],  [130, 255, 255])],   # Blue [cite: 19]
        "SLOW":   [([11,  120, 80],  [25,  255, 255])],   # Orange [cite: 19]
        "START":  [([20,  60,  60],  [35,  255, 255])],   # Yellow [cite: 19]
        "GOAL":   [([80,  60,  60],  [100, 255, 255])],   # Cyan [cite: 21]
    }

    def count_color(roi_hsv, label):
        mask = np.zeros(roi_hsv.shape[:2], dtype=np.uint8)
        for lo, hi in colour_ranges[label]:
            mask |= cv2.inRange(roi_hsv, np.array(lo), np.array(hi))
        return int(np.count_nonzero(mask))

    # ------------------------------------------------------------------
    # FIX 2: Arena size detection using strict validation flags [cite: 36, 37, 38, 39, 40]
    # ------------------------------------------------------------------
    best_size = 8
    best_score = -1
    
    for size in [6, 8, 10, 12]: 
      cs = aw / size          
      starts = 0
      goals  = 0
      for r in range(size):
            for c in range(size):
                cy1, cy2 = int(ay + r * cs), int(ay + (r + 1) * cs)
                cx1, cx2 = int(ax + c * cs), int(ax + (c + 1) * cs)
                cell_roi = hsv[cy1:cy2, cx1:cx2]
                
                if cell_roi.size == 0:
                    continue
                if count_color(cell_roi, "START") > 15:
                    starts += 1
                if count_color(cell_roi, "GOAL") > 15:
                    goals += 1
                    
        # Must locate exactly 1 distinct start and 1 goal element [cite: 22]
    if starts == 1 and goals == 1:
            score = starts + goals
            if score > best_score:
                best_score = score
                best_size  = size

    # Fallback validation mode: execute background scan matching array structures
    if best_score == -1:
        fallback_best_score = -1
        for size in [6, 8, 10, 12]:  
         hits = 0
         for r in range(size):
                for c in range(size):
                    cy1, cy2 = int(ay + r * cs), int(ay + (r + 1) * cs)
                    cx1, cx2 = int(ax + c * cs), int(ax + (c + 1) * cs)
                    cell_roi = hsv[cy1:cy2, cx1:cx2]
                    
                    for lbl in ["DANGER", "SAFE", "REFUEL", "SLOW"]: 
                        if count_color(cell_roi, lbl) > 20:
                            hits += 1
                            break
         if hits > fallback_best_score:
                fallback_best_score = hits
                best_size = size

    arena_size = best_size
    result["arena_size"] = arena_size 
    cs = aw / arena_size

    # ------------------------------------------------------------------
    # Final Matrix Grid Classification Pass
    # ------------------------------------------------------------------
    for r in range(arena_size):
        for c in range(arena_size):
            cy1, cy2 = int(ay + r * cs), int(ay + (r + 1) * cs)
            cx1, cx2 = int(ax + c * cs), int(ax + (c + 1) * cs)
            cell_roi = hsv[cy1:cy2, cx1:cx2]
            
            if cell_roi.size == 0:
                continue
                
            # Compute Alphanumeric string map identifiers (e.g. A1, H8) [cite: 72]
            coord = chr(65 + c) + str(arena_size - r) 
            
            # Target structural text layers explicitly inside the full boundaries [cite: 22, 68]
            if count_color(cell_roi, "START") > 15:
                result["start"] = coord 
                continue
            if count_color(cell_roi, "GOAL") > 15:
                result["goal"] = coord 
                
            # For special navigation cells: target internal zones to avoid checker borders [cite: 68]
            cy = int(ay + r * cs + cs / 2)
            cx = int(ax + c * cs + cs / 2)
            d  = max(2, int(cs * 0.20))
            center_roi = hsv[max(0, cy-d):min(gray.shape[0], cy+d), 
                             max(0, cx-d):min(gray.shape[1], cx+d)]
                             
            for label in ["DANGER", "SAFE", "REFUEL", "SLOW"]: 
                if count_color(center_roi, label) > 5:
                    result["special_cells"][coord] = label
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