## Description
This Python script captures a video or an image file, or uses the camera to capture real-time video, and then displays the frames with the FPS (frames per second) count. It uses the OpenCV library to read and display the frames, and the Numpy library for numerical calculations. It also uses the argparse library to parse command-line arguments.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements
<pre>Python 3
OpenCV
PyTorch
numpy
argparse</pre>

## Installing
Clone the repository to your local machine using the following command:

<pre> git clone https://github.com/your_username/video-fps-analyzer.git </pre>

## Usage
The script takes in the following command-line arguments:

python python_main.py `[-h]` `[-v]` [-v VIDEO] `[-c]` `[--no_show]` `[-d]` [-d DEVICE]

The following arguments are available:
<pre>
-h, --help: show help message and exit.
-v VIDEO, --video VIDEO: path to Video File.
-c, --camera: set this flag to use the camera.
--no_show: don't show output.
-d DEVICE, --device DEVICE: specify the target device to infer on; CPU or GPU. Suitable plugin for the device specified.</pre>

## Example usage:
`bash`
To analyze the FPS of a video file, run the following command:
<pre>python python_main.py -v /path/to/video.mp4</pre>

To analyze the FPS of a camera feed, run the following command:
<pre>python python_main.py -c</pre>

To analyze the FPS of a video file using the GPU, run the following command:
<pre>python python_main.py -v /path/to/video.mp4 -d gpu</pre>


## Output
The script displays the frames with the FPS count on them. It also outputs the average and maximum FPS over all frames to the console.

