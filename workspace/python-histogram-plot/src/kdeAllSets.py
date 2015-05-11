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
f = open(csvString)
csv_f = csv.reader(f)
csv_labels = array(["0.6096","0.5","0.4","0.3048",'0.2','0.1524','0.1','0.0762'])

#only one set of data
my_data = genfromtxt(csvString,delimiter=',')
for x in range(0,8):
    stdev = sqrt(var(my_data[:,x]));
    x_values = range(125, int(math.ceil(max(my_data[:,x])+50)))
    bandwidth = 4
    firstKDE = gaussian_kde(my_data[:,x], bw_method=bandwidth/stdev);
    firstPDF = firstKDE.evaluate(x_values);
    plt.plot(x_values, firstPDF,label=csv_labels[x])
    #print(firstPDF)

plt.title(csvString + " Frequency (KDE-bw="+str(bandwidth)+")")
plt.legend()
deg = u'\N{DEGREE SIGN}'
plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")
plt.show()