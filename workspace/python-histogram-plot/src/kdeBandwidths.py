import csv
from numpy import *
from scipy.stats.distributions import entropy
from scipy.stats.kde import gaussian_kde
from scipy.stats.stats import skew, kurtosis
from statsmodels.nonparametric import kde

import matplotlib.pyplot as plt
import numpy as np
from stat import ST_DEV

# add some sort of function definition?
# name of csv
csvString = 'PFMTileAirflows.csv'
# number of models
numModels = 5;
# number of metrics
numMetrics = 5;
# number of bins
numBins = 8;
# labels
labels = array(["0.6096", "0.3048", "0.1524", '0.0762', "0.0381"])
# labels = array(["0.6096","0.3048","0.1524",'0.0762',"0.0381"])

b = zeros((numModels, numMetrics));

my_data = genfromtxt(csvString, delimiter=',')

# TODO adjust the min/max search a little bit
minValue = min(my_data[:, 0])
maxValue = max(my_data[:, numModels - 1])
# print mean(my_data[:,3])
for x in range (0, numModels):
    maxInterim = max(my_data[:, x])
    if maxInterim > maxValue:
        maxValue = maxInterim
    minInterim = min(my_data[:, x])
    if minInterim < minValue:
        minValue = minInterim
        
rangeVal = maxValue - minValue


# only one set of data
my_data = genfromtxt(csvString, delimiter=',')
bandwidths = array([0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
series = 4
for x in range(0, len(bandwidths)):
    stdev = sqrt(var(my_data[:, series]));
    x_values = range(int(minValue - 0.05 * rangeVal), int(maxValue + 0.05 * rangeVal))
    bandwidth = bandwidths[x]
    firstKDE = gaussian_kde(my_data[:, series], bw_method=bandwidth / stdev);
    firstPDF = firstKDE.evaluate(x_values);
    plt.plot(x_values, firstPDF, label=labels[series] + " bw=" + str(bandwidths[x]))
    # print(firstPDF)

plt.title(csvString + " Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'
plt.xlabel("Airflow Rate (cfm)")
plt.ylabel("Frequency")
plt.show()
