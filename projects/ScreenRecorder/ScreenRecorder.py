import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox

import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = (1920, 1080)  # default screen size
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Use "mp4v" for .mp4 files
fps = 25  # Set FPS to 30 by default
is_recording = False
out = None
prev = 0


def start_recording():
    global is_recording, out, prev, SCREEN_SIZE, fps
    if is_recording:
        messagebox.showwarning("Already Recording", "The screen is already being recorded.")
        return

    output_file = file_entry.get()
    if not output_file:
        messagebox.showerror("Invalid Filename", "Please enter a valid filename for the output.")
        return

    # Ensure the file has a .mp4 extension
    if not output_file.endswith(".mp4"):
        output_file += ".mp4"

    is_recording = True
    out = cv2.VideoWriter(output_file, fourcc, fps, SCREEN_SIZE)
    prev = time.time()

    # Start the screen recording in a separate thread
    recording_thread = threading.Thread(target=record_screen)
    recording_thread.daemon = True  # Ensure the thread ends when the main program ends
    recording_thread.start()


def stop_recording():
    global is_recording, out
    if not is_recording:
        messagebox.showwarning("Not Recording", "No screen recording is in progress.")
        return

    is_recording = False
    out.release()
    messagebox.showinfo("Recording Stopped", "The screen recording has been saved successfully.")


def record_screen():
    global prev, out, fps, is_recording
    while is_recording:
        time_elapsed = time.time_ns() - prev
        img = pyautogui.screenshot()
        if time_elapsed > 1.0 / fps:
            prev = time.time()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get the current mouse position
            mouse_x, mouse_y = pyautogui.position()

            # Draw a circle representing the cursor
            cursor_radius = 10  # You can adjust the size of the cursor
            cursor_color = (0, 255, 0)  # Green color for the cursor
            cv2.circle(frame, (mouse_x, mouse_y), cursor_radius, cursor_color, -1)

            # Write the frame with the cursor drawn on it
            out.write(frame)

        cv2.waitKey(10)  # Adjust the sleep time for smoother recording

    out.release()


def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if output_file:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, output_file)


# Create the main window
root = tk.Tk()
root.title("Screen Recording Tool")

# Create and place widgets
file_label = tk.Label(root, text="Output File:")
file_label.grid(row=0, column=0, padx=10, pady=10)

file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse...", command=select_output_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.grid(row=1, column=2, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()
