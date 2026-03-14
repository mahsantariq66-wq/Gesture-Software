"""
Display module for showing translations on video
"""
import cv2
from config import TEXT_COLOR, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS

class Display:
    def __init__(self):
        self.window_name = "Gesture Translator"
        
    def show_frame(self, frame, translation="", country="", gesture_name=""):
        """
        Display frame with translation overlay
        """
        if frame is None:
            return
            
        # Add text overlay
        if translation:
            # Main translation
            cv2.putText(
                frame,
                f"Translation: {translation}",
                (10, 30),
                TEXT_FONT,
                TEXT_SCALE,
                TEXT_COLOR,
                TEXT_THICKNESS
            )
            
            # Country info
            cv2.putText(
                frame,
                f"Country: {country}",
                (10, 60),
                TEXT_FONT,
                TEXT_SCALE * 0.8,
                (255, 255, 255),
                TEXT_THICKNESS
            )
            
            # Gesture name
            if gesture_name and gesture_name != "Unknown":
                cv2.putText(
                    frame,
                    f"Gesture: {gesture_name}",
                    (10, 90),
                    TEXT_FONT,
                    TEXT_SCALE * 0.8,
                    (200, 200, 200),
                    TEXT_THICKNESS
                )
                
        # Show instructions
        cv2.putText(
            frame,
            "Press 'q' to quit | 'c' to change country",
            (10, frame.shape[0] - 10),
            TEXT_FONT,
            TEXT_SCALE * 0.6,
            (255, 255, 255),
            1
        )
        
        # Display frame
        cv2.imshow(self.window_name, frame)
        
    def close(self):
        """Close display window"""
        cv2.destroyAllWindows()