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

    # 1. Isolate the main square arena grid border, ignoring outside annotations
    _, border_thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
    outer_contours, _ = cv2.findContours(border_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(outer_contours) > 0:
        largest_contour = max(outer_contours, key=cv2.contourArea)
        ax, ay, aw, ah = cv2.boundingRect(largest_contour)
    else:
        ax, ay, aw, ah = 0, 0, image.shape[1], image.shape[0]

    # Highly calibrated HSV thresholds for both solid blocks and thin text lines
    colour_ranges = {
        "DANGER": [([0, 120, 70], [10, 255, 255]), ([170, 120, 70], [180, 255, 255])], # Red
        "SAFE":   [([35, 100, 60], [85, 255, 255])],                                   # Green
        "REFUEL": [([100, 100, 60], [130, 255, 255])],                                  # Blue
        "SLOW":   [([11, 120, 70], [24, 255, 255])],                                   # Orange
        "START":  [([20, 50, 50], [35, 255, 255])],                                     # Yellow 'S'
        "GOAL":   [([80, 50, 50], [100, 255, 255])]                                     # Cyan 'G'
    }

    # Helper function to convert pixel centroids into Alphanumeric grid mappings
    def pixel_to_grid_coordinate(cx, cy, arena_size):
        # Determine cell size dynamically based on the current locked configuration size
        cell_w = aw / arena_size
        cell_h = ah / arena_size
        
        # Calculate relative distance from the inner active arena grid origin
        relative_x = cx - ax
        relative_y = cy - ay
        
        col_idx = int(relative_x // cell_w)
        row_idx = int(relative_y // cell_h)
        
        # Boundary constraints check
        col_idx = max(0, min(arena_size - 1, col_idx))
        row_idx = max(0, min(arena_size - 1, row_idx))
        
        col_letter = chr(65 + col_idx)               # 0 -> 'A', 1 -> 'B'
        row_number = str(arena_size - row_idx)        # Flips orientation: row 0 is top
        return f"{col_letter}{row_number}"

    # 2. STEP 1: Determine Arena Size dynamically using Text Contours
    # The true grid sizing configuration will perfectly map both START and GOAL elements
    detected_markers = {}
    
    for label in ["START", "GOAL"]:
        # Compile mask ranges
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for lo, hi in colour_ranges[label]:
            mask |= cv2.inRange(hsv, np.array(lo), np.array(hi))
            
        # Extract contours matching this specific layout identifier
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        valid_centroids = []
        for c in contours:
            if cv2.contourArea(c) > 8: # Lower floor constraint to drop noise artifacts
                M = cv2.moments(c)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    # Ensure centroid lives inside the active grid area boundaries
                    if ax <= cx <= (ax + aw) and ay <= cy <= (ay + ah):
                        valid_centroids.append((cx, cy))
                        
        if len(valid_centroids) == 1:
            detected_markers[label] = valid_centroids[0]

    # Calculate optimal size match configuration based on text markers alignment
    arena_size = 8  # Fallback default configuration structure
    if len(detected_markers) == 2:
        start_pt = detected_markers["START"]
        goal_pt = detected_markers["GOAL"]
        
        # Test configurations to see which size places markers closest to true cell centers
        best_size_error = float("inf")
        for size in [6, 8, 10, 12]:
            cell_w = aw / size
            cell_h = ah / size
            
            total_error = 0
            for pt in [start_pt, goal_pt]:
                rx, ry = pt[0] - ax, pt[1] - ay
                # Calculate absolute deviation from ideal center pixel layout points
                ideal_cx = (int(rx // cell_w) + 0.5) * cell_w
                ideal_cy = (int(ry // cell_h) + 0.5) * cell_h
                total_error += abs(rx - ideal_cx) + abs(ry - ideal_cy)
                
            if total_error < best_size_error:
                best_size_error = total_error
                arena_size = size

    result["arena_size"] = arena_size

    # 3. STEP 2: Process text marker labels placement directly into results
    if "START" in detected_markers:
        pt = detected_markers["START"]
        result["start"] = pixel_to_grid_coordinate(pt[0], pt[1], arena_size)
    if "GOAL" in detected_markers:
        pt = detected_markers["GOAL"]
        result["goal"] = pixel_to_grid_coordinate(pt[0], pt[1], arena_size)

    # 4. STEP 3: Map Environmental Special Cells using Contour Center Positions
    for label in ["DANGER", "SAFE", "REFUEL", "SLOW"]:
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for lo, hi in colour_ranges[label]:
            mask |= cv2.inRange(hsv, np.array(lo), np.array(hi))
            
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            # Solid blocks are larger than text elements, use a higher area validation floor
            if cv2.contourArea(c) > 100:
                M = cv2.moments(c)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    
                    if ax <= cx <= (ax + aw) and ay <= cy <= (ay + ah):
                        coord = pixel_to_grid_coordinate(cx, cy, arena_size)
                        # Verify it isn't overwriting a text position cell layout
                        if coord != result["start"] and coord != result["goal"]:
                            result["special_cells"][coord] = label
                    
                   


  

   

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