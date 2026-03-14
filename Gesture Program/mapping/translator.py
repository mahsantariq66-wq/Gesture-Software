"""
Translate gestures to meanings based on country
"""
from mapping.loader import MappingLoader

class Translator:
    def __init__(self):
        self.loader = MappingLoader()
        
    def translate(self, gesture_id):
        """
        Translate gesture ID to meaning based on current country
        """
        country_mapping = self.loader.mappings.get(self.loader.current_country, {})
        return country_mapping.get(gesture_id, "Unknown gesture")
        
    def set_country(self, country):
        """Set translation country"""
        return self.loader.set_country(country)
        
    def get_available_countries(self):
        """Get list of available countries"""
        return self.loader.get_countries()
        
    def get_current_country(self):
        """Get current country"""
        return self.loader.get_current_country()