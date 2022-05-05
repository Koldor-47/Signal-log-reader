from datetime import datetime as dt

class Sensor:
    def __init__(self, name, id, raw_data, cfg_data):
        self.config_data = cfg_data
        self.raw_data = raw_data
        self.name = name
        self.id = id
        self._data = []
        self._sampleType = ""
        self.find_sensor_names_cfgfile()
        self.sortData()
    
    def sortData(self):
        for line in self.raw_data:
            line = line.split(" ")
            thetime = dt.strptime(line[0], "%H%M%S.%f")
            sensorData = {"time":thetime, "Value" : line[2]}
            self._data.append(sensorData)

    def find_sensor_names_cfgfile(self):
        self._read_cfg_data_noComment = ""
        for self.line in self.config_data.split("\n"):
            if len(self.line) > 1:
                if self.line[0] != '#':
                    self._read_cfg_data_noComment += self.line + "\n"
        
        sensors = self._read_cfg_data_noComment.split("\n")[1:-2]
        
        for sensor in sensors:
            sensor = sensor.split(" ")
            if sensor[1].split("=")[1] == self.name:
                self._sampleType = sensor[0]      

    def print_raw_data(self):
        print(self.name)
        for num in range(10):
            print(self.raw_data[num])
    
    def print_values(self):
        for data in self._data:
            print(f' Value:{data["Value"]}') 
    
    def print_count(self):
        print(f"data count: {self._data.__len__()}")

    def single_value(self, indexNum):
        return self._data[indexNum]
    
    def print_ID(self):
        print(self.id)

    def sensor_data_list(self):
        sensor_data = []
        for num, line in enumerate(self.raw_data):
            line = line.split(" ")
            sensor_data.append(line[2])
        return sensor_data