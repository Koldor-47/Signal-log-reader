from logging.handlers import RotatingFileHandler
import matplotlib.pyplot as plt
import pandas as pd

import sensor
import SignalLog

test = SignalLog.SignalLog(r"Data\220502_150544.SIL")


#df = pd.DataFrame(test._sensorNames[12]._data)
#df2 = pd.DataFrame(test._sensorNames[11]._data)

#print(df)

#df.rename(columns={'Value': test._sensorNames[12].name}, inplace=True)
#df2.rename(columns={'Value': test._sensorNames[11].name}, inplace=True)

#print(df)


#df3 = pd.merge(df, df2)

#print(df.head(10))
#print(df.drop_duplicates(["time"]).head(10))

#print(df3.drop_duplicates(["time"]))

#dataFile = test.single_sensor_to_csv("HNS_RCP_LOCAL_M_Y")
#plt.plot(df3["HNS_RCP_LOCAL_M_Y"], df3["HNS_RCP_LOCAL_M_X"], "ro")
#plt.xticks(rotation=45)
#plt.show()


sensor_data_test = test.Get_sensor_block_data()

#print(sensor_data_test)
testData_5 = test. All_Sensor_dataFrame(sensor_data_test)

print(test.listSensors())

print(testData_5)

#plt.plot(testData_5["HNS_RIG_HEAD_LOCAL_DEG"])
#plt.xticks(rotation=45)
#plt.show()