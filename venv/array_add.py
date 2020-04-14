import numpy as np
from numpy import genfromtxt
from pathlib import Path
out_arr = np.empty((8, 8),dtype='float32')
fileCount = 0

folder="C:\\Users\\Mike\\PycharmProjects\\impedanceTimeSort\\venv\\data\\processed\\i_3\\"

for file in Path(folder).glob('*.csv'):
       fileCount = fileCount + 1
       new_array = genfromtxt(folder + file.stem + ".csv", delimiter=',',dtype=float)
       out_arr = np.add(new_array, out_arr)
       print(new_array)


print(fileCount)
print(out_arr)

out_arr = np.divide(out_arr, fileCount)

print(out_arr)

np.savetxt("report.csv", out_arr.astype(int), delimiter=",")

# filename1= genfromtxt('Elias_953bb_43915_1120_processed.csv', delimiter=',')
# filename2 = genfromtxt('Elias_953i_43915_1120_processed.csv', delimiter=',')
#
#
# in_arr1 = geek.array(filename1)
# in_arr2 = geek.array(filename2)
#
# print("1st Input array : ", in_arr1)
# print("2nd Input array : ", in_arr2)
#
# out_arr = geek.add(in_arr1, in_arr2)
# print("output added array : ", out_arr)