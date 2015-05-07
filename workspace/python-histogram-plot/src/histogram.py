from numpy import *
import numpy as np
from scipy.stats.stats import skew, kurtosis
import matplotlib.pyplot as plt
import csv
from scipy.stats.distributions import entropy

f = open('ComparableMetrics.csv')
csv_f = csv.reader(f)

numModels = 11;
numMetrics = 4;
a = array([2,3,4])
b = zeros((numModels,numMetrics));

#for row in csv_f:
#    print (row)
    
my_data = genfromtxt('ComparableMetrics.csv',delimiter=',')
#print (my_data)

#Matplotlib has a built-in tex-like 
numBins = 8
minValue = min(my_data[:,0])

maxValue = max(my_data[:,numModels-1])
print mean(my_data[:,3])
for x in range (0,numModels):
    maxInterim = max(my_data[:,x])
    if maxInterim > maxValue:
        maxValue = maxInterim

binWidth = (maxValue-minValue)/(numBins)
newBins=np.arange(minValue,maxValue,binWidth)

for x in range (0,numModels):
    frequency = plt.hist(my_data[:,x], bins=newBins, histtype='step',normed=True,label=labels[x]);
    b[x,0] = mean(my_data[:,x]);
    b[x,1] = var(my_data[:,x]);
    b[x,2] = skew(my_data[:,x]);
    b[x,3] = kurtosis(my_data[:,x]);
    b[x,4] = entropy(frequency[0])

plt.title("Rack Inlet Temperature Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'
#print deg
#print frequency0[0]

plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")

#print range(0,3);

for i in range (0,5):
    print(b[:,i])

#plt.show()

