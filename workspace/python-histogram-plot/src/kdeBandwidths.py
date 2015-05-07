import csv
from numpy import *
from scipy.stats.distributions import entropy
from scipy.stats.kde import gaussian_kde
from scipy.stats.stats import skew, kurtosis
from statsmodels.nonparametric import kde

import matplotlib.pyplot as plt
import numpy as np
from stat import ST_DEV


f = open('ComparableMetrics.csv')
csv_f = csv.reader(f)
csv_labels = array(["Quick","Detailed 24","Detailed 12","Detailed 6"])

#only one set of data
my_data = genfromtxt('ComparableMetrics.csv',delimiter=',')
bandwidths = array([0.2, 0.5, 1.0, 1.5, 2.0, 5.0])
series = 1
for x in range(0, len(bandwidths)):
    stdev = sqrt(var(my_data[:,series]));
    x_values = range(20, int(math.ceil(max(my_data[:,series])+5)))
    bandwidth = bandwidths[x]
    firstKDE = gaussian_kde(my_data[:,series], bw_method=bandwidth/stdev);
    firstPDF = firstKDE.evaluate(x_values);
    plt.plot(x_values, firstPDF,label=csv_labels[series]+" bw="+str(bandwidths[x]))
    #print(firstPDF)

plt.title("Rack Inlet Temperature Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'
plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")
plt.show()