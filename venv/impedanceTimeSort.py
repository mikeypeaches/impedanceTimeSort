import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
import itertools
from operator import itemgetter
from statistics import mean
from pathlib import Path

timeIntervals = set()
# filename = "data\\kevin_953i_43915_1120.csv"
folder="C:\\Users\\Mike\\PycharmProjects\\impedanceTimeSort\\venv\\data\\"

for file in Path(folder).glob('*.csv'):

    print(file)

    lastInterval = 0
    dataByInterval = []
    newArray = np.array([])

    #read in data
    df= pd.read_csv(file, delimiter = ',')

    #convert time data to whole seconds
    intTime= df.Time.astype(int)


    # Create intervals based on length of each relay operation (5 seconds)
    for data in intTime:
        for i in range(0,325,5):
            timeIntervals.add(i)

    # Sort the intervals
    timeIntervalsSorted= sorted(timeIntervals)
    print(timeIntervalsSorted)
    # plt.plot(intTime, df.BioZ, timeIntervalsSorted)
    # plt.show()

    #Creat a new data frame containing the manipulated time values with original BioZ values
    dfSortedData = pd.DataFrame({'Time':intTime, 'BioZ':df.BioZ})

    #group and split data into columns of based on time intervals
    for x in range (1,len(timeIntervalsSorted)):
        print("set", x)
        for index, row in dfSortedData.iterrows():
            if row['Time'] > lastInterval and row['Time'] < timeIntervalsSorted[x]:
                dataByInterval.append(row['BioZ'])
                # print(x, timeIntervalsSorted[x], row['BioZ'])
        #index intervals
        lastInterval = timeIntervalsSorted[x]


        print(mean(dataByInterval))
        print(len(dataByInterval))
        newArray = np.append(newArray, mean(dataByInterval)).astype(int)
        dataByInterval.clear()
    newArray = newArray.reshape(8,8)
    np.savetxt(folder+ "processed\\" + file.stem + "_processed.csv", newArray, delimiter=",")
    print(newArray)
        # clear frames and lists




