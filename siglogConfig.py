
from logging import exception


path = r"C:\Users\nickk\Documents\Code\Python\work\Signal-log-reader\Data\SIGLOGCFG.TXT"

class SiglogConfig:
    def __init__(self, siglogcfg_path):
        self.sigLog_cfg = siglogcfg_path
        try:
            with open(self.sigLog_cfg, 'r') as raw_d:
                self.raw_data = raw_d.readlines()
        except Exception as e:
            print("opps no file Found ", e)