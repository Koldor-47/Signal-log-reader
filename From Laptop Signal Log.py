# Made to Parse the SIGNALLOG data from a log download
from msilib import add_data
import re
from matplotlib import pyplot as plt

lookfor = "HHMMSS.MS"
startOfData = False



class sensor_data:
    def __init__(self, ID, NAME):
        self.time = []
        self.sensor_data = []
        self.id = ID
        self.name = NAME

    def add_data(self, time, sensor_value):
        self.time.append(time)
        self.sensor_data.append(sensor_value)


    def print_data(self):
        print(self.sensor_data)

    def get_raw_data(self, data):
        for line in data:
            line = line.split(" ")
            self.add_data(line[0], line[2])


def find_sensor_names(DataBlob):
    sensors = []
    if re.findall(r"[0-9]{2} [A-Z_]*\n", DataBlob):
        for sensor in re.findall("[0-9]{2} [A-Z_]*\n", DataBlob):
            sensor = sensor.split(" ")
            sensors.append(sensor_data(sensor[0], sensor[1][:-1]))
        
    return sensors
    
def get_sensor_data(DataBlob, amount_of_sensors, theData):
    sensor_data_lines = re.findall(r"[0-9]+.[0-9]+ [0-9]+ -?[0-9]+.[0-9]+", DataBlob)
    for i in sensor_data_lines:
        i = i.split(" ")
        for j in theData:
            if i[1] == j.id:
                j.add_data(i[0], i[2])
    
    return theData
            
        

with open(r"Data/theFile.sil", 'r') as SigData:
    wholeFile = SigData.read()

s_names = find_sensor_names(wholeFile)

testing = get_sensor_data(wholeFile, 18, s_names)


plt.plot( testing[17].sensor_data[:100], testing[16].sensor_data[:100])
plt.show()