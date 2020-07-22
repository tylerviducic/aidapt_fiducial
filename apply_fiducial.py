# by Tyler Viducic and Torri Jeski

import numpy as np
from event import Event
from fiducialCuts import FiducialCuts

# Read in data here 

data_file = '/media/tylerviducic/Elements/aidapt/synthetic/clasfilter2_5M780.npy' # change to your path, obviously

data_array = np.load(data_file)

num_rows, num_columns = data_array.shape

print(num_rows)

for n in range(num_rows):
    event = Event(data_array[n])
    fd = FiducialCuts(event)

    if not fd.check_event_pass():
        print('Did not pass')
        data_array = np.delete(data_array, n)

num_rows, num_columns = data_array.shape

print(num_rows)