# by Tyler Viducic and Torri Jeski

import numpy as np

# Read in data here 

data_file = '/media/tylerviducic/Elements/aidapt/synthetic/clasfilter2_5M780.npy' # change to your path, obviously

data_array = np.load(data_file)

print(data_array.tostring)