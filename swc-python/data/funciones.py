import glob
import numpy as np
import matplotlib.pyplot as plt
#%%#Creando funcion
def visualize(filename):

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()
#%%#Creando funcion
def detect_problems(files):

    data = np.loadtxt(fname=files, delimiter=',')

    if np.max(data, axis=0)[0] == 0 and np.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif np.sum(np.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
#%%#Llamando las funciones
filenames = sorted(glob.glob('inflammation*.csv'))

def offset_mean(data, targetvalue):
    return ((data - np.mean(data)) + targetvalue)

for filename in filenames[:1]:
    print("")
    print(filename)
    visualize(filename)
    detect_problems(filename)
#%%
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('No parameters:')
display()
print('One parameter:')
display(55)
print('Two parameters:')
display(55, 66)
print('Only setting the value of c')
display(c=77)