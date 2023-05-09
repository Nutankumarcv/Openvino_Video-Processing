import argparse
import cv2
import time
import torch
import os

def configure_arguments():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
    arg_parse.add_argument("-c", "--camera", action='store_true', help="Set true if you want to use the camera.")
    arg_parse.add_argument('--no_show', help="Optional. Don't show output.", action='store_true')
    arg_parse.add_argument("-d", "--device", type=str, default='cpu', help="Specify the target device to infer on; CPU or GPU. Suitable plugin for the device specified.")
    return arg_parse

def check_device(device):
    if device == 'gpu':
        if not torch.cuda.is_available():
            raise Exception("GPU not available on this system.")
        else:
            return torch.device('cuda')
    else:
        return torch.device('cpu')

def main(args):
    device = check_device(args["device"])

    if args["video"]:
        if not os.path.exists(args["video"]):
            raise Exception("The specified video file does not exist.")
        cap = cv2.VideoCapture(args["video"])
    elif args["camera"]:
        cap = cv2.VideoCapture(0)
    else:
        raise Exception("No video or camera source specified.")

    if not cap.isOpened():
        if args["video"]:
            raise Exception("Could not open the specified video file.")
        elif args["camera"]:
            raise Exception("Could not open the camera feed.")

    fps_list = []
    max_fps = 0
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        end_time = time.time()
        elapsed_time = end_time - start_time

        try:
            fps = 1 / elapsed_time
        except ZeroDivisionError:
            fps = 0

        start_time = end_time
        fps_list.append(fps)
        max_fps = max(max_fps, fps)

        if not args["no_show"]:
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Output", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

    avg_fps = sum(fps_list) / len(fps_list)
    print(f"Average FPS: {int(avg_fps)}")
    print(f"Maximum FPS: {int(max_fps)}")

if __name__ == "__main__":
    arg_parse = configure_arguments()
    args = vars(arg_parse.parse_args())

    main(args)
