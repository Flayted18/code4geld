# Ordenar 3 numeros de menor a mayor sin usar condicionales ni ciclos.

x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("Los numeros ordenados son: {}, {} y {}".format(a, b, c))
