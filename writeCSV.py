import os
# from dotenv import load_dotenv
import pandas as pd
import numpy as np
# load_dotenv() 
def writeToCSV(mpu6050_ACCEL_vec, mpu6050_GYRO_vec, AK8963_vec):

    fileRoute = os.getenv("path_csv")
    dataArr = []
    for z in list(zip(mpu6050_ACCEL_vec, mpu6050_GYRO_vec, AK8963_vec)):
        subArr = []
        for i in z:
            subArr += i
        dataArr.append(subArr)
    data = pd.DataFrame(dataArr, columns=['Accel_X', 'Accel_Y', 'Accel_Z', 'GYRO_X', 'GYRO_Y', 'GYRO_Z', 'Magn_X', 'Magn_Y', 'Magn_Z'])
    data.to_csv(fileRoute, index=False)


#     import pandas as pd
# cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
# cities.to_csv('cities.csv', index=False)


