import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import os
from pathlib import Path
from re import search
import sensor
import SignalLog




siglog_log_path = r"Data\220502_150544.SIL"
siglof_cfg_path = r"Data\SIGLOGCFG_reduced.TXT"

# This function compares the siglog file and sigcfg file. the way the sensors are logged is setup in the cfg file
# ie some sensor log on time other when a state changes.
def make_Signal_Log(logfile, cfgFile):
    checksum_regex = r"checksum:? [A-Za-z0-9]{8}"
    data_log = ""
    data_cfg = ""
    with open(logfile, 'r') as L_file:
        line = L_file.read()
        if search(checksum_regex, line):
            data_log = search(checksum_regex, line).group()
            data_log = data_log.split(" ")[1]
    
    with open(cfgFile, "rb") as Cfg_file:
        try:
            Cfg_file.seek(-2, os.SEEK_END)
            while Cfg_file.read(1) != b'\n':
                Cfg_file.seek(-2, os.SEEK_CUR)
        except OSError:
            Cfg_file.seek(0)
        
        data_cfg = Cfg_file.readline().decode()
        data_cfg = data_cfg.split(" ")[1]
    
    if data_cfg == data_log:
        signal_logger = SignalLog.SignalLog(siglog_log_path, siglof_cfg_path)

    return signal_logger



if __name__ == "__main__":
    test = make_Signal_Log(siglog_log_path, siglof_cfg_path)

    test.listSensors()
    print(test._sensir_count)
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


    #sensor_data_test = test.Get_sensor_block_data()

    #print(sensor_data_test)
    #testData_5 = test. All_Sensor_dataFrame(sensor_data_test)

    #print(test.listSensors())

    #df5 = pd.DataFrame(testData_5)

    #print(df5.dtypes)
    #df5.to_excel("test.xlsx")
    #print(df5)
    #plt.plot(testData_5["HNS_RIG_HEAD_LOCAL_DEG"])
    #plt.xticks(rotation=45)
    #plt.show()
    #print(df5.loc[df5["ADPE_STATUS"].notnull()])
