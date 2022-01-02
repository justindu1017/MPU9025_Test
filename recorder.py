# import cv2
# import threading
import time
# import os
# from dotenv import load_dotenv


def main(_9025Thread,video, output, queueReturn_Video):

    # time.sleep(0.1)
    # video name in env
    # load_dotenv()

    # frame counter
    i = 0


    # to get fps
    start = time.time()

    # _9025Thread: _9025 thread
    # if _9025 thread stops. stop recording
    print("Recording")
    while _9025Thread.is_alive():
        check, frame = video.read()
        output.write(frame)
        i += 1
        # cv2.imshow('Capturing', frame)
        
    # to get fps
    end = time.time()

    
    video.release()
    output.release()
    print("video time = ", end-start)
    queueReturn_Video.put(end-start)

    return
    # cv2.destroyAllWindows()