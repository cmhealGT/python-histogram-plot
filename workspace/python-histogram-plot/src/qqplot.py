from numpy import *
import numpy as np
from scipy.stats.stats import skew, kurtosis
import matplotlib.pyplot as plt
import csv
from scipy.stats.distributions import entropy
from matplotlib.pyplot import scatter
from matplotlib.markers import MarkerStyle

#add some sort of function definition?
# name of csv
csvString = 'CFDTileAirflows.csv'
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

for i in range (0,numModels):
    my_data[:,i].sort()

marker_style = dict(linestyle=':', color='Black', markersize=10)


plt.title(csvString)
points = len(my_data[:,0])
for i in range(0,numModels-1):
    plt.subplot(2,2, i-3)
    plt.scatter(my_data[:,i],my_data[:,i+1], facecolors='none', edgecolors='Black')
    #plt.title(str(labels[i+1])+"m vs "+str(labels[i])+"m grid")
    x1 = min(my_data[0,i],my_data[0,i+1])
    y1 = x1
    x2 = max(my_data[points-1,i], my_data[points-1,i+1])
    y2 = x2
    plt.plot([x1,x2],[y1,y2],'k-', color='Red')
    plt.xlabel(str(labels[i])+"m grid airflow rate (cfm)")
    plt.ylabel(str(labels[i+1])+"m grid airflow rate (cfm)")
    
plt.figure().tight_layout()   
plt.show()
