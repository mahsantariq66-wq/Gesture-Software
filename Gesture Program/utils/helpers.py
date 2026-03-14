"""
Helper functions for gesture translation
"""
import numpy as np
import math

def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance between two points
    """
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def calculate_angle(point1, point2, point3):
    """
    Calculate angle between three points (in degrees)
    """
    a = np.array([point1.x, point1.y])
    b = np.array([point2.x, point2.y])
    c = np.array([point3.x, point3.y])
    
    ba = a - b
    bc = c - b
    
    # Avoid division by zero
    norm_ba = np.linalg.norm(ba)
    norm_bc = np.linalg.norm(bc)
    
    if norm_ba == 0 or norm_bc == 0:
        return 0
    
    cosine_angle = np.dot(ba, bc) / (norm_ba * norm_bc)
    # Clamp to avoid numerical errors
    cosine_angle = np.clip(cosine_angle, -1, 1)
    angle = np.arccos(cosine_angle)
    
    return np.degrees(angle)

def get_finger_state(hand_landmarks, finger_tips, finger_pips, wrist_index=0):
    """
    Determine if fingers are extended or folded
    Returns a list of booleans [thumb, index, middle, ring, pinky]
    """
    finger_states = []
    
    # Thumb (special case - compare with index finger MCP)
    thumb_tip = hand_landmarks.landmark[finger_tips[0]]
    thumb_ip = hand_landmarks.landmark[finger_pips[0]]
    index_mcp = hand_landmarks.landmark[5]  # Index finger MCP
    
    # Thumb is extended based on position relative to index MCP
    # This is a simplified approach - you may need to adjust
    if thumb_tip.x < index_mcp.x:
        finger_states.append(thumb_tip.x < thumb_ip.x)
    else:
        finger_states.append(thumb_tip.x > thumb_ip.x)
    
    # Other fingers - extended if tip y < pip y
    for i in range(1, 5):
        tip = hand_landmarks.landmark[finger_tips[i]]
        pip = hand_landmarks.landmark[finger_pips[i]]
        finger_states.append(tip.y < pip.y)
    
    return finger_states