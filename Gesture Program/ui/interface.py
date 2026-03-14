"""
Simple UI for country selection
"""
import tkinter as tk
from tkinter import ttk

class CountrySelector:
    def __init__(self, countries, current_country, callback):
        self.callback = callback
        self.window = None
        self.countries = countries
        self.current_country = current_country
        
    def show(self):
        """Show country selection dialog"""
        self.window = tk.Tk()
        self.window.title("Select Country")
        self.window.geometry("300x150")
        
        # Label
        label = tk.Label(self.window, text="Select your country:")
        label.pack(pady=10)
        
        # Dropdown
        self.country_var = tk.StringVar(value=self.current_country)
        dropdown = ttk.Combobox(
            self.window,
            textvariable=self.country_var,
            values=self.countries,
            state="readonly"
        )
        dropdown.pack(pady=5)
        
        # OK button
        ok_button = tk.Button(
            self.window,
            text="OK",
            command=self._on_ok
        )
        ok_button.pack(pady=10)
        
        self.window.mainloop()
        
    def _on_ok(self):
        """Handle OK button click"""
        selected_country = self.country_var.get()
        if selected_country and self.callback:
            self.callback(selected_country)
        self.window.destroy()