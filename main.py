# importing the required packages
# pip install pyautogui opencv-python numpy
import pyautogui
import cv2
import numpy as np
import os

# Dynamically get the screen resolution
resolution = pyautogui.size()

# Update the codec for MP4 format
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Function to generate a unique filename
def get_unique_filename(base_name, extension):
    counter = 1
    filename = f"{base_name}.{extension}"
    while os.path.exists(filename):
        filename = f"{base_name}({counter}).{extension}"
        counter += 1
    return filename

# Update the filename to use a unique name
filename = get_unique_filename("Recording", "mp4")

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
