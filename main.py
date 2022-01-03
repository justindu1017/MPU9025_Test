import threading
import matplotlib.pyplot as plt
import numpy as np
import recorder
import _9025
import writeCSV
import queue
import os 
import cv2
from mpu9250_i2c import *
from dotenv import load_dotenv
import math
import datetime





def plotSave(mpu6050_ACCEL_str,mpu6050_GYRO_str,AK8963_str, mpu6050_ACCEL_vec,mpu6050_GYRO_vec,AK8963_vec,t_vec):
    fig,axs = plt.subplots(3,1,sharex=True)
    # x_Axis = list(range(math.floor(t_vec[-1])+1))
    x_Axis = [(a/2) for a in (range(2*(math.floor(t_vec[-1])+1)))]
    cmap = plt.cm.Set1
    
    # ax = axs[0] # plot accelerometer data

    for zz in range(0,np.shape(mpu6050_ACCEL_vec)[1]):
        data_vec = [ii[zz] for ii in mpu6050_ACCEL_vec]
        # plt.xticks(t_vec)
        axs[zz].plot(t_vec,data_vec,label=mpu6050_ACCEL_str[zz],color=cmap(zz))
        axs[zz].legend(bbox_to_anchor=(1.12,0.9))
        axs[zz].set_xticks(x_Axis, minor=False)
        axs[zz].tick_params(axis="x", labelsize=12) 
        axs[zz].set_ylabel('Acceleration [g]',fontsize=12)

    fig.align_ylabels(axs)
    fig.set_size_inches(18, 10)
    fig.savefig('./output/accel.png', dpi=100)
    plt.close(fig)
    # plt.show()

    fig,axs = plt.subplots(3,1,sharex=True)

    # ax2 = axs[1] # plot gyroscope data
    for zz in range(0,np.shape(mpu6050_GYRO_vec)[1]):
        data_vec = [ii[zz] for ii in mpu6050_GYRO_vec]
        axs[zz].plot(t_vec,data_vec,label=mpu6050_GYRO_str[zz],color=cmap(zz))
        axs[zz].legend(bbox_to_anchor=(1.12,0.9))
        axs[zz].set_xticks(x_Axis, minor=False)
        axs[zz].tick_params(axis="x", labelsize=12) 
        axs[zz].set_ylabel('Angular Vel. [dps]',fontsize=12)

    fig.align_ylabels(axs)
    fig.set_size_inches(18, 10)
    fig.savefig('./output/gyro.png', dpi=100)
    plt.close(fig)
    # plt.show()

    fig,axs = plt.subplots(3,1,sharex=True)


    # ax3 = axs[2] # plot magnetometer data
    for zz in range(0,np.shape(AK8963_vec)[1]):
        data_vec = [ii[zz] for ii in AK8963_vec]
        axs[zz].plot(t_vec,data_vec,label=AK8963_str[zz],color=cmap(zz+6))
        axs[zz].legend(bbox_to_anchor=(1.12,0.9))
        axs[zz].set_xticks(x_Axis, minor=False)
        axs[zz].tick_params(axis="x", labelsize=12) 
        axs[zz].set_ylabel('Magn. Field [Î¼T]',fontsize=12)
        axs[zz].set_xlabel('Time [s]',fontsize=14)

    fig.align_ylabels(axs)
    fig.set_size_inches(18, 10)
    fig.savefig('./output/meg.png', dpi=100)
    plt.close(fig)


def setCamera():
    recorded_Loc = os.getenv("recorded_Loc")
    
    # recording setup
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_BUFFERSIZE, 10)
    vid_cod = cv2.VideoWriter_fourcc(*'mp4v')

    # fps = 20
    # video size = (640, 480)
    output = cv2.VideoWriter(recorded_Loc, vid_cod, 20.0, (640, 480))
    return video, output

def setPath(path):
    try:
        if(not os.path.isdir(path)):
            os.mkdir(path)
        
    except:
        print("Err when createing output folder!!!!!!")
        exit

if __name__ == "__main__":
    load_dotenv()
    
    num_of_points = 1000
    setPath(path=os.getenv("output_Path"))
    video, output = setCamera()

    queueReturn_9025 = queue.Queue()
    queueReturn_Video = queue.Queue()

    t = threading.Thread(target=_9025.start, args=(queueReturn_9025, num_of_points))
    t2 = threading.Thread(target=recorder.main, args=(t,video, output, queueReturn_Video, ))
    t.start()
    t2.start()
    t.join()
    t2.join()

    
    mpu6050_ACCEL_str = queueReturn_9025.get()
    mpu6050_GYRO_str = queueReturn_9025.get()
    AK8963_str = queueReturn_9025.get()
    mpu6050_ACCEL_vec = queueReturn_9025.get()
    mpu6050_GYRO_vec = queueReturn_9025.get()
    AK8963_vec = queueReturn_9025.get()
    t_vec = queueReturn_9025.get()
    sample_rate = queueReturn_9025.get()
    Time9025 = queueReturn_9025.get()

    plotSave(mpu6050_ACCEL_str,mpu6050_GYRO_str,AK8963_str, mpu6050_ACCEL_vec,mpu6050_GYRO_vec,AK8963_vec,t_vec)
    with open(os.getenv("path_csv"), "w") as f:
        f.write("########## The sample rate is: "+ str(sample_rate))
        f.write("\n########## recorded point: "+ str(num_of_points))
        f.write("\n########## total reoceded time: "+ str(queueReturn_Video.get()))
        f.write("\n########## total 9025 time: "+ str(Time9025))
        f.write("\n########## time Stemp: "+ str(datetime.datetime.now()))
        f.write("\n\n")




    writeCSV.writeToCSV(mpu6050_ACCEL_vec, mpu6050_GYRO_vec, AK8963_vec)

        

    print("FINISH")