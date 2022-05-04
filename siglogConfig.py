
from logging import exception

class SiglogConfig:
    def __init__(self, siglogcfg_path):
        self.sigLog_cfg = siglogcfg_path
        with open(self.sigLog_cfg, 'r') as raw_d:
            self.raw_data = raw_d.readlines()
