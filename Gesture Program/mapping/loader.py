"""
Load country-specific gesture mappings
"""
import json
from config import MAPPINGS_FILE

class MappingLoader:
    def __init__(self):
        self.mappings = self._load_mappings()
        self.current_country = "USA"
        
    def _load_mappings(self):
        """Load country mappings from JSON file"""
        try:
            with open(MAPPINGS_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default mappings if file not found
            return {
                "USA": {
                    "thumbs_up": "Good job!",
                    "peace": "Peace",
                    "ok": "OK",
                    "pointing": "Look there",
                    "open_palm": "Stop",
                    "closed_fist": "Fight!",
                    "unknown": "Gesture not recognized"
                }
            }
            
    def get_countries(self):
        """Get list of available countries"""
        return list(self.mappings.keys())
        
    def set_country(self, country):
        """Set current country for translations"""
        if country in self.mappings:
            self.current_country = country
            return True
        return False
        
    def get_current_country(self):
        """Get current country"""
        return self.current_country