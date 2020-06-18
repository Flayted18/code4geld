import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob("inflammation*.csv"))
filenames = filenames[0:3]

for file in filenames:
    print(file)
    
    data = np.loadtxt(fname=file, delimiter=",")
    
    fig = plt.figure(figsize=(10.0, 3.0))
    
    axes1 = fig.add_subplot(1, 3, 1)
    axes1 = fig.add_subplot(1, 3, 2)
    axes1 = fig.add_subplot(1, 3, 3)
    
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

max_inflammation_0 = np.max(data, axis=0)[0]
max_inflammation_20 = np.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif np.sum(np.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')