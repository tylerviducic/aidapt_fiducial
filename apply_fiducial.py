# by Tyler Viducic and Torri Jeski

import numpy as np
from dataManager import DataManager
import fiducialCuts as fd

# Read in data here 

data_file = '/media/tylerviducic/Elements/aidapt/synthetic/clasfilter2_5M780.npy' # change to your path, obviously

data_array = np.load(data_file)

for event in data_array:
    current_event = DataManager(event)
    print(current_event.proton)
