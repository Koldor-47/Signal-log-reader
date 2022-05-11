from dataclasses import dataclass

@dataclass
class Sensor:
    id : str
    alias : str
    sample_type : str
    sample_period : int
    data : list
