"""
Camera input module for capturing video frames
"""
import cv2
import threading
from config import CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT, CAMERA_FPS

class Camera:
    def __init__(self):
        self.cap = None
        self.frame = None
        self.is_running = False
        self.lock = threading.Lock()
        
    def start(self):
        """Start camera capture in a separate thread"""
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, CAMERA_FPS)
        
        if not self.cap.isOpened():
            raise Exception("Could not open camera")
        
        self.is_running = True
        self.thread = threading.Thread(target=self._update_frame)
        self.thread.daemon = True
        self.thread.start()
        
    def _update_frame(self):
        """Continuously update the latest frame"""
        while self.is_running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.frame = cv2.flip(frame, 1)  # Mirror for natural feel
                    
    def get_frame(self):
        """Get the latest frame"""
        with self.lock:
            return self.frame.copy() if self.frame is not None else None
            
    def stop(self):
        """Stop camera capture"""
        self.is_running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        if self.cap:
            self.cap.release()
            
    def is_opened(self):
        """Check if camera is opened"""
        return self.cap is not None and self.cap.isOpened()