import re
from dataclasses import dataclass

@dataclass
class signal:
    id: int
    sample_type : str
    alias : str


good_id = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13]

path_cfg =r"Data/SIGLOGCFG_reduced.TXT"
path_sig =r"Data/220502_150544.SIL"

with open(path_cfg, "r") as Data:
    sigcfg_raw_text = Data.readlines()


with open(path_sig, "r") as Data:
    siglog_raw_text = Data.read()


good_data = re.findall(r"[0-9]{6}.[0-9]{3} [0-9]{2} -?[0-9]+.[0-9]*", siglog_raw_text)

def find_sensor_names_cfgfile():
    _read_cfg_data_noComment = ""
    for line in config_data.split("\n"):
        if len(line) > 1:
            if line[0] != '#':
               _read_cfg_data_noComment += line + "\n"

def id_to_names(raw_data):
    id_names = re.findall(r"[0-9]{2} [A-Z_]+", raw_data)
    names = {}
    for line in id_names:
        line = line.split(" ")
        names[line[0]] = line[1]

    return names

def Get_periodic_data(listOfIds, raw_data, id_names):
    block = {}
    total_data = []
    lengthOfID = len(listOfIds)
    added_ids = []
    for line in raw_data:
        line = line.split(" ")
        if len(block) == 0:
            block["time"] = line[0]
        block[id_names[line[1]]] = line[2]

        if (len(block) + 1) == lengthOfID:
            total_data.append(block)
            block = {}
    
    return total_data

signal_names = id_to_names(siglog_raw_text)
t = Get_periodic_data(good_id, good_data, signal_names)


print(t[:4])
