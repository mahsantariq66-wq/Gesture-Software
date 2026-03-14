"""
Configuration settings for the gesture translator
"""
import os

# Camera settings
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 30

# Processing settings
FRAME_SKIP = 2  # Process every 2nd frame for performance
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

# Gesture recognition settings
STATIC_GESTURE_MODE = False
MAX_NUM_HANDS = 2
MODEL_COMPLEXITY = 1

# Output settings
ENABLE_SPEECH = True
TEXT_COLOR = (0, 255, 0)  # Green
TEXT_FONT = 0
TEXT_SCALE = 0.7
TEXT_THICKNESS = 2

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MAPPINGS_FILE = os.path.join(DATA_DIR, 'mappings.json')
GESTURES_FILE = os.path.join(DATA_DIR, 'gestures.json')

# Default settings
DEFAULT_COUNTRY = "USA"