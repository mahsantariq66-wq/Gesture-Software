"""
Frame preprocessing module
"""
import cv2
import numpy as np

class Preprocessor:
    def __init__(self):
        self.frame_count = 0
        
    def process(self, frame):
        """
        Prepare frame for gesture detection
        Returns processed frame and whether to process this frame
        """
        if frame is None:
            return None, False
            
        self.frame_count += 1
        
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        return frame_rgb, True