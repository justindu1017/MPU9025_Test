from mpu9250_i2c import *
import smbus,time,datetime
import numpy as np
import matplotlib.pyplot as plt
import writeCSV

def start():
    plt.style.use('ggplot') # matplotlib visual style setting

    time.sleep(1) # wait for mpu9250 sensor to settle

    ii = 300 # number of points
    t1 = time.time() # for calculating sample rate

    # prepping for visualization
    mpu6050_ACCEL_str = ['accel-x','accel-y','accel-z']
    mpu6050_GYRO_str = ['gyro-x','gyro-y','gyro-z']
    AK8963_str = ['mag-x','mag-y','mag-z']
    mpu6050_ACCEL_vec,mpu6050_GYRO_vec,AK8963_vec,t_vec = [],[],[],[]

    print('recording data')
    for ii in range(0,ii):
        print(ii)
        try:
            ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
            mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
        except:
            continue
        t_vec.append(time.time()) # capture timestamp
        AK8963_vec.append([mx,my,mz])
        mpu6050_ACCEL_vec.append([ax,ay,az])
        mpu6050_GYRO_vec.append([wx,wy,wz])

    print('sample rate accel: {} Hz'.format(ii/(time.time()-t1))) # print the sample rate
    t_vec = np.subtract(t_vec,t_vec[0])


    # plot the resulting data in 3-subplots, with each data axis
    # fig,axs = plt.subplots(3,3,figsize=(12,7),sharex=True)


    
    # ===============================================================================
    # fig,axs = plt.subplots(3,1,sharex=True)

    # cmap = plt.cm.Set1

    # ax = axs[0] # plot accelerometer data

    # for zz in range(0,np.shape(mpu6050_ACCEL_vec)[1]):
    #     data_vec = [ii[zz] for ii in mpu6050_ACCEL_vec]
    #     axs[zz].plot(t_vec,data_vec,label=mpu6050_ACCEL_str[zz],color=cmap(zz))
    #     axs[zz].legend(bbox_to_anchor=(1.12,0.9))
    #     axs[zz].set_ylabel('Acceleration [g]',fontsize=12)

    # fig.align_ylabels(axs)
    # plt.show()

    # fig,axs = plt.subplots(3,1,sharex=True)

    # cmap = plt.cm.Set1
    # # ax2 = axs[1] # plot gyroscope data
    # for zz in range(0,np.shape(mpu6050_GYRO_vec)[1]):
    #     data_vec = [ii[zz] for ii in mpu6050_GYRO_vec]
    #     axs[zz].plot(t_vec,data_vec,label=mpu6050_GYRO_str[zz],color=cmap(zz))
    #     axs[zz].legend(bbox_to_anchor=(1.12,0.9))
    #     axs[zz].set_ylabel('Angular Vel. [dps]',fontsize=12)

    # fig.align_ylabels(axs)
    # plt.show()

    # fig,axs = plt.subplots(3,1,sharex=True)

    # cmap = plt.cm.Set1

    # # ax3 = axs[2] # plot magnetometer data
    # for zz in range(0,np.shape(AK8963_vec)[1]):
    #     data_vec = [ii[zz] for ii in AK8963_vec]
    #     axs[zz].plot(t_vec,data_vec,label=AK8963_str[zz],color=cmap(zz+6))
    #     axs[zz].legend(bbox_to_anchor=(1.12,0.9))
    #     axs[zz].set_ylabel('Magn. Field [Î¼T]',fontsize=12)
    #     axs[zz].set_xlabel('Time [s]',fontsize=14)

    # fig.align_ylabels(axs)
    # plt.show()
    # ===============================================================================

    writeCSV.writeToCSV(mpu6050_ACCEL_vec, mpu6050_GYRO_vec, AK8963_vec)
    print("FINISH")