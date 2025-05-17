import cv2
import numpy as np
import pyautogui

#Set the screen resolution
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# Set the output video file name and codec
output_file = 'screen_recording.mp4'

# Set the frames per second (FPS) for the recording
fps = 30.0

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, resolution)

# Define the recording duration in seconds
recording_duration = 5

# Start the recording duration in seconds
for _ in range(int(fps * recording_duration)):
    # Capture the screen
    screen = pyautogui.screenshot()

    # Convert the image to a numpy array and BGR format for OpenCV
    frame = np.array(screen)

    # Convert the color from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

# Release the VideoWriter object and close all OpenCV windows
out.release()