# Import the libraries:
import numpy as np
import cv2
import time
import os
import argparse
import torch

#Configuration Parameters:
def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
    arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
    arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    arg_parse.add_argument("-d", "--device", type=str, default='cpu', help="Device to use for processing (cpu or gpu)")
    args = vars(arg_parse.parse_args())

    return args

args = argsParser()

if args['device'] == 'gpu' and torch.cuda.is_available():
    device = torch.device('gpu')
else:
    device = torch.device('cpu')

if args['camera']:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(args['video'])

# used to record the time when we processed last frame and current frame
prev_frame_time = 0
new_frame_time = 0

# total fps counter
total_fps = 0
frame_counter = 0
max_fps = 0

# Reading the video file:
while(cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
    gray = frame

    # resizing the frame size
    #gray = cv2.resize(gray, (1080, 720))

    new_frame_time = time.time()

    # Calculating the fps:

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    max_fps = max(max_fps, fps)

    # increment total fps and frame counter
    total_fps += fps
    frame_counter += 1

    # converting the fps into integer
    fps = int(fps)
    fps = str(fps)
    print("FPS: ", fps)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (40, 40, 255), 3, cv2.LINE_AA)

    # displaying the frame with fps
    cv2.imshow('frame', gray)

    # press 'Q' if you want to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# calculate average fps and display
avg_fps = int(total_fps / frame_counter) if frame_counter > 0 else 0
avg_fps_str = "Average FPS: " + str(avg_fps)
print(avg_fps_str)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(gray, avg_fps_str, (7, 140), font, 3, (40, 40, 255), 3, cv2.LINE_AA)

# calculate max fps and display
max_fps_str = "Max FPS: " + str(int(max_fps))
print(max_fps_str)
cv2.putText(gray, max_fps_str, (7, 210), font, 3, (40, 40, 255), 3, cv2.LINE_AA)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
