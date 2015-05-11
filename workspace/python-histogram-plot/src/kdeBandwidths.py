import csv
from numpy import *
from scipy.stats.distributions import entropy
from scipy.stats.kde import gaussian_kde
from scipy.stats.stats import skew, kurtosis
from statsmodels.nonparametric import kde

import matplotlib.pyplot as plt
import numpy as np
from stat import ST_DEV

csvString = 'FFDTileAirflows.csv'
csv_labels = array(["0.6096","0.5","0.4","0.3048"])

#only one set of data
my_data = genfromtxt(csvString,delimiter=',')
bandwidths = array([0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
series = 1
for x in range(0, len(bandwidths)):
    stdev = sqrt(var(my_data[:,series]));
    x_values = range(125, int(math.ceil(max(my_data[:,series])+50)))
    bandwidth = bandwidths[x]
    firstKDE = gaussian_kde(my_data[:,series], bw_method=bandwidth/stdev);
    firstPDF = firstKDE.evaluate(x_values);
    plt.plot(x_values, firstPDF,label=csv_labels[series]+" bw="+str(bandwidths[x]))
    #print(firstPDF)

plt.title(csvString + " Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'
plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")
plt.show()