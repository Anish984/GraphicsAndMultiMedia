import tkinter as tk
import cv2
import threading
import sys
import os

# --- Global Flags ---
# Used to signal the video thread to stop when the Tkinter window closes
is_running = False 

def capture_video_feed():
    """
    Captures live video from the default webcam and displays it 
    in a separate OpenCV window. This function runs in a thread.
    """
    global is_running
    
    # Use 0 for the default webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not access the webcam (Index 0). Check connections or permissions.")
        return

    window_name = "LIVE WEBCAM FEED (Press 'q' or close window to stop)"
    is_running = True
    
    while is_running and cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame.")
            break
        
        # Display the resulting frame
        cv2.imshow(window_name, frame)
        
        # Check for user input: 'q' key stops the feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup when the loop breaks
    is_running = False
    cap.release()
    cv2.destroyAllWindows()
    print("Video capture stopped.")

def start_capture_thread():
    """Starts the capture_video_feed function in a background thread."""
    global is_running
    if not is_running:
        print("Starting webcam capture...")
        # Start the video capture in a new thread
        threading.Thread(target=capture_video_feed).start()
    else:
        print("Capture is already running.")

def stop_capture():
    """Sets the flag to stop the video capture thread."""
    global is_running
    if is_running:
        is_running = False
        print("Signal sent to stop capture.")
    
# --- GUI Setup ---

def on_closing():
    """Handles window closing, ensuring the video thread is stopped."""
    stop_capture()
    root.destroy()

root = tk.Tk()
root.title("Webcam/Mic Capture Interface")
root.geometry("300x150")

# Start Button
btn_start = tk.Button(
    root, 
    text="Start Webcam Video", 
    command=start_capture_thread, 
    width=20, 
    height=2
)
btn_start.pack(pady=10)

# Stop Button
btn_stop = tk.Button(
    root, 
    text="Stop Capture", 
    command=stop_capture, 
    width=20, 
    height=2,
    fg='red' # Make it stand out
)
btn_stop.pack(pady=5)

# Set the protocol handler for closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    root.mainloop()
