import numpy as np
import os
from numpy import genfromtxt
from pathlib import Path

folder="C:\\Users\\Mike\\PycharmProjects\\impedanceTimeSort\\venv\\data\\processed\\i\\"

# Number of file names with "*_processed.csv" substring
N = len([file for file in Path(folder).glob('*_processed.csv')]);
out_arr = np.zeros([N, 8, 8],dtype='float32');
fileCount = 0

# Renamed from "list" to avoid conflict w/ python key word "list"
my_list = []
# File count, initialized at zero
n = 0;
# For each file...
for file in Path(folder).glob('*_processed.csv'):
    # Append file to my_list
    my_list.append(file)
    # Load 8x8
    new_array = genfromtxt(folder + file.stem + ".csv", delimiter=',', dtype=float);
    # Store n'th 8x8 in out_arr
    out_arr[n,:,:] = new_array;
    # Increment file count
    n += 1;
# Initialize 8x8 standard deviation storage
std_arr = np.zeros([8,8]);
# For each row (of 8)...
for row_idx in range(8):
    # For each column (of 8..
    for col_idx in range(8):
        # The (row_idx,col_idx) entry of std_array is
        # populated with the standard deviation of all
        # (row_idx,col_idx) entries across N (=4) total
        std_arr[row_idx,col_idx] = np.std([
            out_arr[n,row_idx,col_idx] for n in range(N)
        ]);
np.savetxt("report_std.csv", std_arr.astype(int), delimiter=",")