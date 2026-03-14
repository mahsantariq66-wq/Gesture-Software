"""
Hand detection module using MediaPipe
"""
import mediapipe as mp
import cv2
from config import STATIC_GESTURE_MODE, MAX_NUM_HANDS, MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=STATIC_GESTURE_MODE,
            max_num_hands=MAX_NUM_HANDS,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Landmark indices for finger tips and PIPs
        self.finger_tips = [4, 8, 12, 16, 20]  # Thumb tip to pinky tip
        self.finger_pips = [3, 6, 10, 14, 18]  # Thumb IP to pinky PIP
        
    def detect(self, frame_rgb):
        """
        Detect hands in the frame
        Returns annotated frame and hand landmarks
        """
        results = self.hands.process(frame_rgb)
        
        # Convert back to BGR for OpenCV
        frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        
        hand_landmarks_list = []
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on frame
                self.mp_drawing.draw_landmarks(
                    frame_bgr,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
                hand_landmarks_list.append(hand_landmarks)
                
        return frame_bgr, hand_landmarks_list
    
    def get_finger_landmarks(self, hand_landmarks):
        """Extract fingertip and PIP coordinates"""
        tips = []
        pips = []
        
        for tip_idx, pip_idx in zip(self.finger_tips, self.finger_pips):
            tips.append(hand_landmarks.landmark[tip_idx])
            pips.append(hand_landmarks.landmark[pip_idx])
            
        return tips, pips