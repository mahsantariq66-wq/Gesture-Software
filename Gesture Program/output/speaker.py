"""
Text-to-speech output module
"""
import pyttsx3
import threading

class Speaker:
    def __init__(self):
        self.engine = None
        self.last_spoken = ""
        self.speech_enabled = True
        self.lock = threading.Lock()
        
    def _init_engine(self):
        """Initialize TTS engine"""
        if self.engine is None:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            
    def speak(self, text):
        """
        Speak the translated text (if different from last spoken)
        """
        if not self.speech_enabled or text == self.last_spoken or text == "Unknown gesture":
            return
            
        with self.lock:
            self._init_engine()
            self.last_spoken = text
            # Use threading to avoid blocking
            thread = threading.Thread(target=self._speak_thread, args=(text,))
            thread.daemon = True
            thread.start()
            
    def _speak_thread(self, text):
        """Speak in separate thread"""
        self.engine.say(text)
        self.engine.runAndWait()
        
    def enable(self, enabled=True):
        """Enable/disable speech"""
        self.speech_enabled = enabled