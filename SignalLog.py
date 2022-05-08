import re
import sensor as sn
import pandas as pd
from datetime import datetime as dt



class SignalLog:
    _file_name =""
    _cfg_path_name = ""
    _dataRows = 0
    _sensorNames = []
    _cfg_sensorNames = []
    _read_log_Data = ""
    _read_cfg_data = ""
    _sensir_count = 0


    def __init__(self, filePath, cfgFilePath):
        self._file_name = filePath
        self._cfg_path_name = cfgFilePath
        self._read_log_Data = self.read_raw_data(self._file_name)
        self._read_cfg_data = self.read_raw_data(self._cfg_path_name)
        self.find_sensor_names()
        self._sensir_count = len(self._sensorNames)


    def read_raw_data(self, fileToRead):
        readFile = ""
        with open(fileToRead, 'r') as SigData:
            readFile = SigData.read()
        return readFile

    def find_sensor_names(self):
        sensors = []
        if re.findall(r"[0-9]{2} [A-Z_]*\n", self._read_log_Data):
            for sensor in re.findall("[0-9]{2} [A-Z_]*\n", self._read_log_Data):
                sensor = sensor.split(" ")
                searchDataString = "[0-9]+.[0-9]+ " + sensor[0] + " -?[0-9]+.[0-9]+"
                rawData = re.findall(searchDataString, self._read_log_Data)
                sensor_dict = sn.Sensor(sensor[1].strip(), sensor[0], rawData, self._read_cfg_data)
                sensor_dict.sortData()
                sensors.append(sensor_dict)
        
        self._sensorNames = sensors


    def listSensors(self):
        for sensor in self._sensorNames:
            print(f"ID -> {sensor.id} | Name: {sensor.name} | {sensor._sampleType}")




