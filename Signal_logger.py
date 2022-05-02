from logging.handlers import RotatingFileHandler
import matplotlib.pyplot as plt
import pandas as pd

import sensor
import SignalLog

test = SignalLog.SignalLog(r"Data\220428_104205.SIL")


df = pd.DataFrame(test._sensorNames[17]._data)
df2 = pd.DataFrame(test._sensorNames[16]._data)

#print(df)

df.rename(columns={'Value': test._sensorNames[17].name}, inplace=True)
df2.rename(columns={'Value': test._sensorNames[16].name}, inplace=True)

#print(df)


df3 = pd.merge(df, df2)

#print(df.head(10))
#print(df.drop_duplicates(["time"]).head(10))

#print(df3.drop_duplicates(["time"]))

#dataFile = test.single_sensor_to_csv("HNS_RCP_LOCAL_M_Y")

plt.plot(df3["HNS_RCP_LOCAL_M_Y"], df3["HNS_RCP_LOCAL_M_X"], "ro")
plt.xticks(rotation=45)
plt.show()


#sensor_data_test = test.test_fun2()

#print(sensor_data_test[0])
#test.test_fun2b(sensor_data_test)
