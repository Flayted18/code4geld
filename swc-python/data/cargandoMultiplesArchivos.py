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