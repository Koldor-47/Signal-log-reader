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

          
    def Get_sensor_block_data(self):
        data = []
        block = []
        lines_of_one_block = 18

        for line in re.findall("[0-9]+.[0-9]+ [0-9]+ -?[0-9]+.*[0-9]*", self._readData):
            block.append(line)
            sub_block_id = line.split(" ")[1]
            if int(sub_block_id) >= lines_of_one_block:
                data.append(block)
                block = []

        
        return data
    
    def All_Sensor_dataFrame(self, bigBlob):
        # trying to make a dict of each row Then add each row to a list then add to pandas as a DataFrame
        #
        # {Time : time of first event in group of sensors, Each sensor Name: [list of sensor values update each iteration of  the first loop]}
        #
        # Returns a Pandas Dataframe of all the sensors
        #
        allData = []

        # Return a dict of ID => Sensors Names
        sensor_name_data = self.make_sensor_dict()

        # Each Blob should each sensor Once
        for num, blob in enumerate(bigBlob):
            data_blob = {}     
            data_blob["time"] = blob[0].split(" ")[0]

            for d in blob:
                split_d = d.split(" ")
                sensor_id = split_d[1]
                sensorName = sensor_name_data[sensor_id]
                data_blob[sensorName] = split_d[2]

            
            allData.append(data_blob)
        
        return allData
                


