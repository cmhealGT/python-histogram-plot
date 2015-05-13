import csv
from numpy import *
from scipy.stats.distributions import entropy
from scipy.stats.kde import gaussian_kde
from scipy.stats.stats import skew, kurtosis
from statsmodels.nonparametric import kde

import matplotlib.pyplot as plt
import numpy as np
from stat import ST_DEV

csvString = 'PFMTileAirflows.csv'
# number of models
numModels = 5;
csv_labels = array(["0.6096", "0.3048", "0.1524", '0.0762', "0.0381"])

# csv_labels = array(["0.6096","0.5","0.4","0.3048",'0.2','0.1524','0.1','0.0762'])

# only one set of data
my_data = genfromtxt(csvString, delimiter=',')

# find min/max values for airflows
maxVal = math.ceil(max(my_data[:, 0]))
minVal = math.floor(min(my_data[:, 0]))
for x in range(1, numModels):
    modelMax = math.ceil(max(my_data[:, x]))
    modelMin = math.floor(min(my_data[:, x]))
    if modelMax > maxVal:
        maxVal = modelMax
    if modelMin < minVal:
        minVal = modelMin  
rangeVal = maxVal - minVal

# construct plots
for x in range(0, numModels):
    stdev = sqrt(var(my_data[:, x]));
    x_values = range(int(minVal - 0.05 * rangeVal), int(maxVal + 0.05 * rangeVal))
    bandwidth = 1
    firstKDE = gaussian_kde(my_data[:, x], bw_method=bandwidth / stdev);
    firstPDF = firstKDE.evaluate(x_values);
    plt.plot(x_values, firstPDF, label=csv_labels[x])
    
    # print(firstPDF)

plt.title(csvString + " Frequency (KDE-bw=" + str(bandwidth) + ")")
plt.legend()
plt.axis([minVal - 0.05 * rangeVal, maxVal + 0.05 * rangeVal, 0, 0.25])
deg = u'\N{DEGREE SIGN}'
plt.xlabel("Airflow Rate (cfm)")
# plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")
plt.show()
