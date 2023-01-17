import re
import datetime as dt
from turtle import color
import matplotlib.pyplot as plt
import numpy as np


def read_data(dataFile):
    with open(dataFile, 'r') as data:
        raw_data = data.readlines()
    
    return raw_data



regex_sensor = "[0-9]{2} [A-Za-z_]*"


if __name__ == "__main__":
    siglog_raw_data = read_data("Data//K32.txt")
    #siglog_raw_data = input("Please enter a .sil file")

    sensors = []
    sensors_dict = {}


    for line in siglog_raw_data:
        if re.match(regex_sensor, line):
            sensors.append(line)
            sensors_dict[line.split(" ")[0]] = []



    for sensor in sensors:
        sensor = sensor.split(" ")[0]
        for line in siglog_raw_data:
            regex_data = re.compile(f"[0-9]*.[0-9]* {sensor} *")
            if re.match(regex_data, line):
                sensor_id = line.split(" ")[1]
                timeTxt = line.split(" ")[0]
                theTime = dt.datetime.strptime(timeTxt, "%H%M%S.%f")
                sesnor_data = [theTime, line.split(" ")[2][:-1]]
                if sensor_id in sensors_dict:
                    sensors_dict[sensor_id].append(sesnor_data)



    x_axis = np.array([x[0] for x in sensors_dict["01"]])
    y_axis = [float(x[1]) for x in sensors_dict["01"]]
    
    x_axis2 = np.array([x[0] for x in sensors_dict["02"]])
    y_axis2 = [float(x[1]) for x in sensors_dict["02"]]


    
    fig, (ax, ax2) = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0)
    ax.plot(x_axis, y_axis)

    ax2.plot(x_axis2, y_axis2, color='green')

    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

    plt.show()
