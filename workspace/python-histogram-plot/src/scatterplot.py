from numpy import *
import numpy as np
from scipy.stats.stats import skew, kurtosis
import matplotlib.pyplot as plt
import csv
from scipy.stats.distributions import entropy
from matplotlib.pyplot import scatter

f = open('ComparableMetrics.csv')
csv_f = csv.reader(f)

b = zeros((4,5));

#for row in csv_f:
#    print (row)
    
my_data = genfromtxt('ComparableMetrics.csv',delimiter=',')

for i in range (0,4):
    b[i,0] = mean(my_data[:,i]);
    b[i,1] = var(my_data[:,i]);
    b[i,2] = skew(my_data[:,i]);
    b[i,3] = kurtosis(my_data[:,i]);
    
a = array([500,1500,2500,2800])

plt.scatter(a, b[:,0], color="Red")
plt.scatter(a, b[:,1], color="Blue")
plt.scatter(a, b[:,2], color="Yellow")
plt.scatter(a, b[:,3], color="Black")
plt.show()