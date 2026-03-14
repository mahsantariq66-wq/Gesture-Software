"""
Gesture classifier module
"""
import json
import os
from utils.helpers import get_finger_state
from config import GESTURES_FILE

class GestureClassifier:
    def __init__(self):
        self.gestures = self._load_gestures()
        
    def _load_gestures(self):
        """Load gesture definitions from file"""
        try:
            if os.path.exists(GESTURES_FILE):
                with open(GESTURES_FILE, 'r') as f:
                    return json.load(f)
            else:
                print(f"Gestures file not found at {GESTURES_FILE}, using defaults")
                return self._get_default_gestures()
        except Exception as e:
            print(f"Error loading gestures: {e}")
            return self._get_default_gestures()
    
    def _get_default_gestures(self):
        """Return default gestures if file not found"""
        return {
            "thumbs_up": {
                "name": "Thumbs Up",
                "finger_pattern": [True, False, False, False, False]
            },
            "peace": {
                "name": "Peace Sign",
                "finger_pattern": [False, True, True, False, False]
            },
            "ok": {
                "name": "OK Sign",
                "finger_pattern": [True, True, False, False, False]
            },
            "pointing": {
                "name": "Pointing",
                "finger_pattern": [False, True, False, False, False]
            },
            "open_palm": {
                "name": "Open Palm",
                "finger_pattern": [True, True, True, True, True]
            },
            "closed_fist": {
                "name": "Closed Fist",
                "finger_pattern": [False, False, False, False, False]
            }
        }
            
    def classify(self, hand_landmarks):
        """
        Classify the gesture based on finger states
        Returns gesture ID and name
        """
        if not hand_landmarks:
            return "unknown", "Unknown"
            
        # Get finger states [thumb, index, middle, ring, pinky]
        finger_tips = [4, 8, 12, 16, 20]
        finger_pips = [3, 6, 10, 14, 18]
        finger_states = get_finger_state(hand_landmarks, finger_tips, finger_pips)
        
        # Compare with known gestures
        for gesture_id, gesture_info in self.gestures.items():
            if finger_states == gesture_info["finger_pattern"]:
                return gesture_id, gesture_info.get("name", gesture_id)
                
        return "unknown", "Unknown"