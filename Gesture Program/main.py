"""
Main application file - Real-time Gesture Translator
"""
import cv2
import sys
from config import FRAME_SKIP, ENABLE_SPEECH, DEFAULT_COUNTRY

# Import modules
from input.camera import Camera
from preprocessing.processor import Preprocessor
from recognition.detector import HandDetector
from recognition.classifier import GestureClassifier
from mapping.translator import Translator
from output.display import Display
from output.speaker import Speaker
from ui.interface import CountrySelector

class GestureTranslator:
    def __init__(self):
        # Initialize all modules
        self.camera = Camera()
        self.preprocessor = Preprocessor()
        self.detector = HandDetector()
        self.classifier = GestureClassifier()
        self.translator = Translator()
        self.display = Display()
        self.speaker = Speaker() if ENABLE_SPEECH else None
        
        # Set default country
        self.translator.set_country(DEFAULT_COUNTRY)
        
        # State variables
        self.running = False
        self.current_translation = ""
        self.current_gesture = ""
        
    def change_country(self, new_country):
        """Callback for country selection"""
        if self.translator.set_country(new_country):
            print(f"Country changed to: {new_country}")
            
    def show_country_selector(self):
        """Show country selection UI"""
        selector = CountrySelector(
            self.translator.get_available_countries(),
            self.translator.get_current_country(),
            self.change_country
        )
        selector.show()
        
    def run(self):
        """Main application loop"""
        try:
            # Start camera
            self.camera.start()
            print("Camera started. Press 'q' to quit, 'c' to change country")
            
            self.running = True
            frame_count = 0
            
            while self.running:
                # Get frame from camera
                frame = self.camera.get_frame()
                
                # Preprocess frame
                processed_frame, should_process = self.preprocessor.process(frame)
                
                if processed_frame is not None and should_process:
                    # Detect hands
                    annotated_frame, hand_landmarks_list = self.detector.detect(processed_frame)
                    
                    # Classify gesture for the first hand detected
                    if hand_landmarks_list:
                        gesture_id, gesture_name = self.classifier.classify(hand_landmarks_list[0])
                        
                        # Translate gesture
                        translation = self.translator.translate(gesture_id)
                        
                        # Update state
                        self.current_translation = translation
                        self.current_gesture = gesture_name
                        
                        # Speak translation if enabled
                        if self.speaker:
                            self.speaker.speak(translation)
                    else:
                        self.current_translation = ""
                        self.current_gesture = ""
                        
                    # Display frame with translation
                    self.display.show_frame(
                        annotated_frame,
                        self.current_translation,
                        self.translator.get_current_country(),
                        self.current_gesture
                    )
                    
                    # Check for key presses
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        self.running = False
                    elif key == ord('c'):
                        self.show_country_selector()
                        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.cleanup()
            
    def cleanup(self):
        """Clean up resources"""
        print("Cleaning up...")
        self.camera.stop()
        self.display.close()
        cv2.destroyAllWindows()
        print("Application closed")

def main():
    """Entry point"""
    print("=== Real-time Gesture Translator ===")
    print("Initializing...")
    
    app = GestureTranslator()
    
    # Show country selector at start
    app.show_country_selector()
    
    # Run main application
    app.run()

if __name__ == "__main__":
    main()