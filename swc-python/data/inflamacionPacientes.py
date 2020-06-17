#axis = 0 es para Filas y axis = 1 es para Columnas
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(data)
image = plt.imshow(data) #Grafico de Calor
plt.show()
ave_inflammation = np.mean(data, axis=0) #Grafico Lineal
ave_plot = plt.plot(ave_inflammation)
plt.show()
max_plot = plt.plot(np.max(data, axis = 0))
plt.show()
min_plot = plt.plot(np.min(data, axis = 0))
plt.show()
#%%
#Acomodar el espacio para las Graficas
fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)#(Filas, Columnas, Orden Izq-Der)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0), drawstyle='steps-mid')
axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0), drawstyle='steps-mid')
axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0), drawstyle='steps-mid')

fig.tight_layout()

plt.show()


#%% #Apilando las graficas Verticalmente
fig = plt.figure(figsize=(17.0, 25.0)) #Que tan grande sera la Trama

axes1 = fig.add_subplot(4, 1, 1)
axes2 = fig.add_subplot(4, 1, 2)   
axes3 = fig.add_subplot(4, 1, 3)
axesstd = fig.add_subplot(4, 1, 4)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0), drawstyle='steps-mid')

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0), drawstyle='steps-mid')

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0), drawstyle='steps-mid')

axesstd.set_ylabel('std')
axesstd = plt.plot(np.std(data, axis=0), drawstyle='steps-mid')



fig.tight_layout()

plt.show()
#%%Bucle For
for var in range(0,5): #Range(x, y, z) x Inicia, y Finaliza - 1, z Incrementa.
    print(var)

"""
for idx, val in enumerate(a_list):
    # Do something using idx and val
    """
#%%
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = list(salsa)        # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)

sasa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_sasa = sasa        # <-- my_salsa and salsa point to the *same* list data in memory
sasa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_sasa)
#%%
counts = [2, 4, 6, 8, 10]
repeats = counts * 2 #El * en listas cumple la funcion de replicar y concatenar.
print(repeats)  # "counts + counts"
#%%
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sond = months[8:len(months)]
print("Using len() to get last entry:", sond)



