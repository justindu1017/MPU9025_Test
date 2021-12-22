import queue

queue = queue.queue()
thread_ = threading.Thread(
                target=target_method,
                name="Thread1",
                args=[params, queue],
                )
thread_.start()
thread_.join()
queue.get()

def target_method(self, params, queue):
 """
 Some operations right here
 """
 your_return = "Whatever your object is"
 queue.put(your_return)


# import threading
# import time

# # 子執行緒的工作函數
# def job():
#   for i in range(10):
#     print("Child thread:", i)
#     time.sleep(1)

# # 建立一個子執行緒
# t = threading.Thread(target = job)

# # 執行該子執行緒
# t.start()

# # 主執行緒繼續執行自己的工作
# for i in range(3):
#   print("Main thread:", i)
#   time.sleep(1)

# # 等待 t 這個子執行緒結束
# t.join()

# print("Done.")


# #!/usr/bin/env python
# #! --*-- coding:utf-8 --*--
# import cv2
# import time
 
# if __name__ == '__main__' :
#     # 启动默认相机
#     video = cv2.VideoCapture(0)
     
#     # 获取 OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
#     # 对于 webcam 不能采用 get(CV_CAP_PROP_FPS) 方法 
#     # 而是：
#     if int(major_ver)  < 3 :
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#     else :
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
     
#     # Number of frames to capture
#     num_frames = 120
#     print("Capturing {0} frames".format(num_frames))
 
#     # Start time
#     start = time.time()
#     # Grab a few frames
#     for i in range(0, num_frames):
#         ret, frame = video.read()
#     # End time
#     end = time.time()
 
#     # Time elapsed
#     seconds = end - start
#     print("Time taken : {0} seconds".format(seconds))
 
#     # 计算FPS，alculate frames per second
#     fps  = num_frames / seconds
#     print("Estimated frames per second : {0}".format(fps))
 
#     # 释放 video
#     video.release()