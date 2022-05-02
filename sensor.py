from datetime import datetime as dt

class Sensor:
    def __init__(self, name, id, raw_data):
        self.raw_data = raw_data
        self.name = name
        self.id = id
        self._data = []
        self.sortData()
    
    def sortData(self):
        for line in self.raw_data:
            line = line.split(" ")
            thetime = dt.strptime(line[0], "%H%M%S.%f")
            sensorData = {"time":thetime, "Value" : line[2]}
            self._data.append(sensorData)
        

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