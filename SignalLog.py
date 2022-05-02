import re
import sensor as sn
import pandas as pd


class SignalLog:
    _file_name =""
    _dataRows = 0
    _sensorNames = []
    _readData = ""

    def __init__(self, filePath):
        self._file_name = filePath
        self.read_signal_log()
        self.find_sensor_names()
    
    def read_signal_log(self):
        with open(self._file_name, 'r') as SigData:
            self._readData = SigData.read()

    def find_sensor_names(self):
        sensors = []
        if re.findall(r"[0-9]{2} [A-Z_]*\n", self._readData):
            for sensor in re.findall("[0-9]{2} [A-Z_]*\n", self._readData):
                sensor = sensor.split(" ")
                searchDataString = "[0-9]+.[0-9]+ " + sensor[0] + " -?[0-9]+.[0-9]+"
                rawData = re.findall(searchDataString, self._readData)
                sensor_dict = sn.Sensor(sensor[1].strip(), sensor[0], rawData)
                sensor_dict.sortData()
                sensors.append(sensor_dict)
        
        self._sensorNames = sensors

    def listSensors(self):
        for sensor in self._sensorNames:
            print(f"ID -> {sensor.id} | Name: {sensor.name}")

    def make_sensor_dict(self):
        test = {}
        for sensor in self._sensorNames:
            test[sensor.id] = sensor.name
        
        return test
    
    def single_sensor_to_csv(self, sensorsName):
        id_of_sensor = 0
        for id in self._sensorNames:
            if id.name == sensorsName:
                the_id = int(id.id) - 1
                df = pd.DataFrame(self._sensorNames[the_id]._data)
                df.rename(columns={"Value" : sensorsName}, inplace=True)
                df.set_index("time", inplace=True)
                df.to_csv(f"{sensorsName}.csv")

          
    def all_sensors_toCsv(self):
        df = pd.DataFrame(self._sensorNames[0]._data)
        df.rename(columns={"Value" : self._sensorNames[0].name}, inplace=True)
        for sen in range(1, len(self._sensorNames)):
            temp_df = pd.DataFrame(self._sensorNames[sen]._data)
            temp_df.rename(columns={"Value" : self._sensorNames[sen].name}, inplace=True)
            df = pd.merge(df, temp_df, how="left", on=["time"])
        
        print(df)


    def test_fun2(self):
        data = []
        block = []
        lines_of_one_block = 16
        line_count = 0
        for line in re.findall("[0-9]+.[0-9]+ [0-9]+ -?[0-9]+.[0-9]+", self._readData):
            block.append(line)
            line_count += 1
            if line_count >= lines_of_one_block:
                data.append(block)
                block = []
                line_count = 0
        
        return data
    
    def test_fun2b(self, bigBlob):
        allData = []
        sensor_name_data = self.make_sensor_dict()

        for num, blob in enumerate(bigBlob):
            data_blob = {}
            theNum = str(num)
            s_name = sensor_name_data[blob[theNum.zfill(2)].split(" ")[1]]
            data_blob["time"] = blob[num].split(" ")[0]
            data_blob[s_name] = []
            for d in blob:
                d = d.split(" ")
                data_blob[s_name].append(d[2])
            
            allData.append(data_blob)
        
        print(allData[0])
                


