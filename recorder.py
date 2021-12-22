import cv2
import threading
import time
import os
from dotenv import load_dotenv


def main(args):
    load_dotenv()
    i = 0

    recorded_Loc = os.getenv("recorded_Loc")
    nowTime = time.time()

    first_frame = None
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_BUFFERSIZE, 10)
    vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
    # fps = 20
    # video size = (640, 480)
    output = cv2.VideoWriter(recorded_Loc, vid_cod, 20.0, (640, 480))

    start = time.time()
    while args.is_alive():
        check, frame = video.read()
        output.write(frame)
        i += 1

        cv2.imshow('Capturing', frame)
        

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    end = time.time()

    print("the frame is ", i / (end - start))
    
    video.release()
    output.release()
    cv2.destroyAllWindows()