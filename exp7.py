import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from playsound import playsound
import cv2
import threading
import sys
import os

# --- Configuration (Files to Use) ---
AUDIO_FILE = 'sample_audio.mp3'
VIDEO_FILE = 'sample_video.mp4'
IMAGE_FILE = 'sample_image.jpg'
DEFAULT_IMAGE_SIZE = (300, 300)

class MultimediaApp:
    """A simple multimedia player using Tkinter, OpenCV, and Pillow."""

    def __init__(self, master):
        self.master = master
        master.title("Multimedia Player App")
        
        # Initialize an attribute to hold the image reference
        self.current_image = None

        # --- GUI Widgets ---
        
        # Panel for displaying the image
        self.panel = tk.Label(master)
        self.panel.pack(pady=10)

        # Buttons
        self.btn_img = tk.Button(master, text="Show Image", command=self.load_image)
        self.btn_img.pack(pady=5)

        # Audio and Video playback must be run in a separate thread 
        # to prevent the GUI from freezing (blocking the mainloop).
        self.btn_audio = tk.Button(
            master, 
            text="Play Audio", 
            command=lambda: threading.Thread(target=self.play_audio).start()
        )
        self.btn_audio.pack(pady=5)

        self.btn_video = tk.Button(
            master, 
            text="Play Video", 
            command=lambda: threading.Thread(target=self.play_video).start()
        )
        self.btn_video.pack(pady=5)

    # --- Multimedia Logic ---

    def play_audio(self):
        """Plays the audio file in the background."""
        if not os.path.exists(AUDIO_FILE):
             print(f"Error: Audio file not found at '{AUDIO_FILE}'")
             return
        
        try:
            playsound(AUDIO_FILE)
        except Exception as e:
            print(f"Error playing audio: {e}")

    def play_video(self):
        """Plays the video file using OpenCV in a separate window."""
        cap = cv2.VideoCapture(VIDEO_FILE)

        if not cap.isOpened():
            print(f"Error: Could not open video file at '{VIDEO_FILE}'")
            return

        window_name = "Video Player (Press 'q' to stop)"
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Use cv2.namedWindow to control the window behavior
            cv2.imshow(window_name, frame)
            
            # The waitKey is necessary to refresh the window and listen for keyboard input
            # The value '25' gives a frame rate of about 40 FPS
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

    def load_image(self):
        """Loads, resizes, and displays an image in the Tkinter window."""
        try:
            # 1. Load the image using PIL
            img = Image.open(IMAGE_FILE)
            
            # 2. Resize
            img = img.resize(DEFAULT_IMAGE_SIZE)
            
            # 3. Convert to a format Tkinter can display
            img_tk = ImageTk.PhotoImage(img)
            
            # 4. Update the label/panel
            self.panel.configure(image=img_tk)
            
            # CRITICAL: Store a reference to prevent the image from being 
            # garbage collected (which would make the image disappear)
            self.current_image = img_tk
            
        except FileNotFoundError:
            self.panel.configure(text=f"Error: Image file not found at '{IMAGE_FILE}'")
        except Exception as e:
            self.panel.configure(text=f"Error loading image: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    # Ensure necessary multimedia files exist for a cleaner startup
    print("Initializing Multimedia App. Ensure sample files are in the same directory.")
    
    root = tk.Tk()
    app = MultimediaApp(root)
    root.mainloop()
