# Basic Lane Detection Project

This project is a simple implementation of lane detection using computer vision techniques. The goal is to identify and highlight lane markings on a road using a camera feed. This project serves as an educational and foundational step in understanding how lane detection works in the context of autonomous vehicles and driver assistance systems.

## Features

- Detects straight lane markings on roads.
- Highlights the detected lanes in real time.
- Provides a visual output with annotated lanes on the original video feed.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- Numpy library

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/basic-lane-detection.git
   cd basic-lane-detection
#Install the required libraries:
pip install opencv-python numpy

#Run the lane detection script:
python lane_detection.py
--------------------------------------------
How It Works:

The lane detection process involves the following steps:
1.Capturing video frames from a camera feed.
2.Applying image processing techniques to enhance lane visibility.
3.Detecting lane markings using color filtering and edge detection.
4.Using the Hough Transform to identify lines in the image.
5.Filtering and fitting the lines to identify the left and right lane boundaries.
6.Extrapolating the detected lines to cover the visible road area.
7.Overlaying the detected lanes on the original video frames.
8.Displaying the real-time video output with highlighted lanes.

Customization
You can adjust parameters such as color thresholds, edge detection parameters, and region of interest (ROI) coordinates to optimize lane detection for different scenarios.

Acknowledgments
This project is inspired by the need to understand the basics of lane detection in the field of computer vision and autonomous driving.
