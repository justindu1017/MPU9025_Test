import cv2
import threading
import time
import os
from dotenv import load_dotenv


def main(args):
    start = time.time()

    # time.sleep(0.1)
    # video name in env
    load_dotenv()

    # frame counter
    i = 0

    recorded_Loc = os.getenv("recorded_Loc")
    
    # recording setup
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_BUFFERSIZE, 10)
    vid_cod = cv2.VideoWriter_fourcc(*'mp4v')

    # fps = 20
    # video size = (640, 480)
    output = cv2.VideoWriter(recorded_Loc, vid_cod, 20.0, (640, 480))

    # to get fps
    start = time.time()

    # args: _9025 thread
    # if _9025 thread stops. stop recording
    print("Recording")
    while args.is_alive():
        check, frame = video.read()
        output.write(frame)
        i += 1
        # cv2.imshow('Capturing', frame)
        
    # to get fps
    end = time.time()

    
    video.release()
    output.release()
    print("video time = ", end-start)

    return
    # cv2.destroyAllWindows()