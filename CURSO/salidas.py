v = "otro texto"
n = 10
print("Un texto,",v,"y un numero",n)
#%%
c = "Un texto, {} y un numero {}".format(v, n)
print(c)

print("Un texto, {0} y un numero {1}".format(v, n))

print("Un texto, {1} y un numero {0}".format(v, n))
# Un texto, 10 y un numero otro texto
#%%Alinear a la derecha
print( "{:>30}". format("palabra"))
#Alinear a la izquierda
print( "{:30}". format("palabra"))
#Alinear al centro
print( "{:^30}". format("palabra"))

#%%# Truncamiento
print( "{:.3}". format("palabra")) # a 3 caracteres
print( "{:>30.3}". format("palabra"))# Alinear y truncar
#%%# Formateo de numero entero, rellenar con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
#%%# Formateo de numeros flotantes, rellenar con espacios
print("{:.2f}".format(3.1415926))
#-----------------------------
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21)) 