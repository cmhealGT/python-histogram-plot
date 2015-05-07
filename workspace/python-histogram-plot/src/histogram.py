from numpy import *
import numpy as np
from scipy.stats.stats import skew, kurtosis
import matplotlib.pyplot as plt
import csv
from scipy.stats.distributions import entropy

f = open('ComparableMetrics.csv')
csv_f = csv.reader(f)

a = array([2,3,4])
b = zeros((4,5));

#for row in csv_f:
#    print (row)
    
my_data = genfromtxt('ComparableMetrics.csv',delimiter=',')
#print (my_data)

#Matplotlib has a built-in tex-like 
numBins = 8
minValue = min(my_data[:,0])

maxValue = max(my_data[:,3])
print mean(my_data[:,3])
for x in range (0,3):
    maxInterim = max(my_data[:,x])
    if maxInterim > maxValue:
        maxValue = maxInterim

binWidth = (maxValue-minValue)/(numBins)
newBins=np.arange(minValue,maxValue,binWidth)

frequency0 = plt.hist(my_data[:,0], bins=newBins, histtype='step',normed=True,label='Quick');
frequency1 = plt.hist(my_data[:,1], bins=newBins, histtype='step',normed=True,alpha=0.5,label='Detailed 24');
frequency2 = plt.hist(my_data[:,2], bins=newBins, histtype='step',normed=True,alpha=0.5,label='Detailed 12');
frequency3 = plt.hist(my_data[:,3], bins=newBins, histtype='step',normed=True,alpha=0.5, label='Detailed 6');
plt.title("Rack Inlet Temperature Frequency")
plt.legend()
deg = u'\N{DEGREE SIGN}'
#print deg
print frequency0[0]

plt.xlabel("Temperature ("+deg + "C)")
plt.ylabel("Frequency")

print range(0,3)
for i in range (0,4):
    b[i,0] = mean(my_data[:,i]);
    b[i,1] = var(my_data[:,i]);
    b[i,2] = skew(my_data[:,i]);
    b[i,3] = kurtosis(my_data[:,i]);

b[0,4] = entropy(frequency0[0]);
b[1,4] = entropy(frequency1[0]);
b[2,4] = entropy(frequency2[0]);
b[3,4] = entropy(frequency3[0]);

print(b)

#plt.show()

