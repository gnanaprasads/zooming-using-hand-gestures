# zooming-using-hand-gestures
This project is a hand gesture-controlled image viewer built using Python with OpenCV and the cvzone library. It allows users to zoom and pan images using hand gestures detected via the webcam. The application features a simple graphical interface where users can load images from a specified folder and manipulate them in real-time using hand movements.

Features:

Hand Gesture Control: Zoom in/out and pan the image using hand gestures.
Image Navigation: Move between images using keyboard controls.
Adjustable Zoom: Use a trackbar or mouse wheel to adjust the zoom level.
Error Handling: Robust handling for image resizing and bounds checking.
README.md

markdown
Copy code
# Hand Gesture-Controlled Image Viewer

## Overview

This project demonstrates a hand gesture-controlled image viewer using Python, OpenCV, and the cvzone library. The application allows users to zoom and pan images in real-time using hand gestures detected through a webcam.

## Features

- **Hand Gesture Control:** Zoom in/out and pan images with hand gestures.
- **Image Navigation:** Use keyboard shortcuts to switch between images.
- **Adjustable Zoom:** Modify zoom level with a trackbar or mouse wheel.
- **Robust Error Handling:** Manages image resizing and window bounds effectively.

## Requirements

- Python 3.x
- OpenCV
- cvzone

You can install the required libraries using pip:

pip install opencv-python cvzone
How to Run
Clone this repository:

git clone https://github.com/gnanaprasads/zooming-using-hand-gestures.git
Navigate to the project directory:


cd hand-gesture-image-viewer
Make sure you have a folder named images in the project directory with the images you want to view.

Run the script:


python main.py

Controls:
Zoom In/Out: Use the mouse wheel or the trackbar slider in the "Controls" window.
Move Image: Use the index finger gesture to move the image.
Next Image: Press n to load the next image.
Previous Image: Press p to load the previous image.
Quit: Press q to exit the application.

Notes:
Ensure your webcam is functional and properly connected.
The application works best with clear and well-lit environments for accurate hand gesture detection.
License
This project is licensed under the MIT License. See the LICENSE file for details.
