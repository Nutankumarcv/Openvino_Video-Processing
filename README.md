# Description
This Python script captures a video or an image file, or uses the camera to capture real-time video, and then displays the frames with the FPS (frames per second) count. It uses the OpenCV library to read and display the frames, and the Numpy library for numerical calculations. It also uses the argparse library to parse command-line arguments.

Requirements
Python 3
OpenCV
numpy
argparse


Usage
The script takes in the following command-line arguments:

python fps_counter.py [-h] [-v VIDEO] [-i IMAGE] [-c CAMERA] [-o OUTPUT] [-d DEVICE]

-v or --video: path to video file
-i or --image: path to image file
-c or --camera: set to True if using the camera
-o or --output: path to optional output video file
-d or --device: set to cpu or gpu to specify the device for processing

Example usage:
bash
Copy code
python fps_counter.py -v video.mp4 -d gpu


Output
The script displays the frames with the FPS count on them. It also outputs the average and maximum FPS over all frames to the console.
