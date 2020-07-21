# used to get information from synthetic datafile
import numpy as np

class DataManager:

    def __init__(self, event_array):
        self.event_array = event_array
        self.proton = (event_array[2], event_array[5], event_array[8], event_array[11])
        self.pi_plus = (event_array[3], event_array[6], event_array[9], event_array[12])
        self.pi_minus = (event_array[4], event_array[7], event_array[10], event_array[13])        

    def get_proton_phi(self):
        return 