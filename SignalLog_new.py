import re
import sensor as sn
import pandas as pd
from datetime import datetime as dt



class SignalLog:
    _raw_log_data = []
    regexString = ""
    _read_log_Data = ""
    _read_cfg_data = ""
    _siglog_sensor_data = ""
    _sigcfg_sensor_data = ""
    _signals = []

    def __init__(self, filePath, cfgFilePath):
        self.regexString = "[0-9]+.[0-9]+ [0-9]+ -?[0-9]+.[0-9]+"   
        self._file_name = filePath
        self._cfg_path_name = cfgFilePath
        self._read_log_Data = self.read_raw_data(self._file_name)
        self._read_cfg_data = self.read_raw_data(self._cfg_path_name)
        self._siglog_sensor_data = self.raw_sensor_sig_info(self._read_log_Data)
        self._sigcfg_sensor_data = self.find_sensor_names_cfgfile(self._read_cfg_data)
        self._raw_log_data = re.findall(self.regexString, self._read_log_Data)
        self._signals = self.makeSensor(self._sigcfg_sensor_data, self._siglog_sensor_data)


    def read_raw_data(self, fileToRead):
        readFile = ""
        with open(fileToRead, 'r') as SigData:
            readFile = SigData.read()
        return readFile

    def raw_sensor_sig_info(self, raw_data):
        sensor_regex = r"[0-9]{2} [A-Z_]+"
        sigLof_sensor = re.findall(sensor_regex, raw_data)

        return sigLof_sensor
    
    def find_sensor_names_cfgfile(self, raw_data):
        _read_cfg_data_noComment = []
        for line in raw_data.split("\n"):
            if len(line) > 1:
                if line[0] != '#':
                   _read_cfg_data_noComment.append(line)
        
        return _read_cfg_data_noComment[1:-1]


    def makeSensor(self, sigcfg, siglog):
        period = 0
        d = zip(sigcfg, siglog)
        signal_list = []
        for cfg, log in d:
            data_form = []
            period = 0
            cfg = cfg.split(" ")
            log = log.split(" ")
            if len(cfg) == 4:
                period = int(cfg[3].split("=")[1])
            signal_list.append(sn.Sensor(log[0], log[1], cfg[0], period, data_form ))
        
        return signal_list


    def get_peroidic_data(self, sensors, signal_data):
        id_list = []
        count = 0
        my_signal_data = []
        for sig in sensors:
            if sig.sample_type == "AnalogSignalPeriodicSampleLogger":
                id_list.append(sig.id)
                my_signal_data.append(sig)
        
        row_list = []
        row = {}
        Sensor_id = my_signal_data

        for line in signal_data:
            line_s = line.split(" ")
            for sensor in my_signal_data:
                if len(row) == 0:
                    row["time"] = line_s[0]
                
                if sensor.id in id_list:
                    row[sensor.alias] = line_s[2]
                    Sensor_id.remove(sensor)
                    break
            

            if len(row) <= len(id_list):
                continue
            elif len(row) > len(id_list):
                row_list.append(row)
                Sensor_id = my_signal_data        
                row = {}
            
        
        return row_list
                    



