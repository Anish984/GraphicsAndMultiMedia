import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import threading
import os
import sys

# --- Configuration (Files to Use - ENSURE THESE EXIST!) ---
AUDIO_FILE = 'sample_audio.mp3'
IMAGE_FILE = 'sample_image.jpg'
DEFAULT_TEXT = "Multimedia Demo Ready."
DEFAULT_IMAGE_SIZE = (300, 300)

class SimpleMultimediaDashboard:
    """A single-user interface to demonstrate basic multimedia handling."""

    def __init__(self, master):
        self.master = master
        master.title("Simple Multimedia Dashboard")
        
        # Attribute to hold the image reference
        self.current_image = None

        # --- Display Panel (Label used for Text/Image) ---
        self.panel = tk.Label(master, text=DEFAULT_TEXT, height=15, width=40, relief=tk.GROOVE)
        self.panel.pack(pady=10, padx=10)

        # --- Button Frame ---
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # 1. Text Button
        tk.Button(button_frame, text="Display Text", command=self.display_text).pack(side=tk.LEFT, padx=10)

        # 2. Image Button
        tk.Button(button_frame, text="Show Image", command=self.load_image).pack(side=tk.LEFT, padx=10)

        # 3. Audio Button (Requires Threading)
        # Use lambda to start the play_audio function in a background thread
        tk.Button(
            button_frame, 
            text="Play Audio", 
            command=lambda: threading.Thread(target=self.play_audio, daemon=True).start()
        ).pack(side=tk.LEFT, padx=10)

    # --- Multimedia Logic ---

    def display_text(self):
        """Displays simple text on the panel."""
        # Clear any previous image reference
        self.current_image = None
        self.panel.configure(image='', text="Text message displayed successfully!")

    def load_image(self):
        """Loads, resizes, and displays an image on the panel."""
        if not os.path.exists(IMAGE_FILE):
             self.panel.configure(text=f"ERROR: Image file '{IMAGE_FILE}' not found.")
             return
        
        try:
            img = Image.open(IMAGE_FILE)
            img = img.resize(DEFAULT_IMAGE_SIZE, Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            
            # Update the panel to show the image
            self.panel.configure(image=img_tk, text="") 
            
            # CRITICAL: Keep a reference to prevent garbage collection
            self.current_image = img_tk
            
        except Exception as e:
            self.panel.configure(text=f"Error loading image: {e}")

    def play_audio(self):
        """Plays the audio file in the background (blocking operation)."""
        if not os.path.exists(AUDIO_FILE):
             print(f"ERROR: Audio file '{AUDIO_FILE}' not found.")
             return
        
        print("Playing audio...")
        try:
            # playsound is a blocking call, hence the use of threading
            playsound(AUDIO_FILE)
            print("Audio finished.")
        except Exception as e:
            print(f"Error playing audio: {e}")

# --- Main Execution ---

if __name__ == "__main__":
    # Check for required library dependencies
    try:
        # We check for playsound to give the user an error if they haven't installed it
        from playsound import playsound
    except ImportError:
        print("-" * 50)
        print("WARNING: 'playsound' library not found.")
        print("Audio button functionality will fail.")
        print("Please install it: pip install playsound")
        print("-" * 50)
        
    root = tk.Tk()
    app = SimpleMultimediaDashboard(root)
    root.mainloop()
