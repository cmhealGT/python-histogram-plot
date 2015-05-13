from numpy import *
import numpy as np
from scipy.stats.stats import skew, kurtosis
import matplotlib.pyplot as plt
import csv
from scipy.stats.distributions import entropy

#add some sort of function definition?
# name of csv
csvString = 'PFMTileAirflows.csv'
# number of models
numModels = 5;
# number of metrics
numMetrics = 5;
# number of bins
numBins = 8;
# labels
labels = array(["0.6096","0.3048","0.1524",'0.0762',"0.0381"])
#labels = array(["0.6096","0.3048","0.1524",'0.0762',"0.0381"])

b = zeros((numModels,numMetrics));

my_data = genfromtxt(csvString,delimiter=',')

#TODO adjust the min/max search a little bit
minValue = min(my_data[:,0])
maxValue = max(my_data[:,numModels-1])
#print mean(my_data[:,3])
for x in range (0,numModels):
    maxInterim = max(my_data[:,x])
    if maxInterim > maxValue:
        maxValue = maxInterim
    minInterim = min(my_data[:,x])
    if minInterim < minValue:
        minValue = minInterim
        

binWidth = (maxValue-minValue)/(numBins)
newBins=np.arange(minValue,maxValue,binWidth)

#TODO process array only once for speedup?
for x in range (0,numModels):
    frequency = plt.hist(my_data[:,x], bins=newBins, histtype='step',normed=True,label=labels[x]);
    b[x,0] = mean(my_data[:,x]);
    b[x,1] = var(my_data[:,x]);
    b[x,2] = skew(my_data[:,x]);
    b[x,3] = kurtosis(my_data[:,x]);
    b[x,4] = entropy(frequency[0])

plt.title(csvString+" Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'

plt.xlabel("Airflow Rate (cfm)")
plt.ylabel("Frequency")

for i in range (0,5):
    print(b[:,i])

plt.show()