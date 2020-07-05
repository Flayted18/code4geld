n = int("10") # Pasar a entero
f = float("10.5") # Pasar a flotante
c = "Un texto y un numero " + str(10) + " " + str(3.14) # Convertir en cadena

b = bin(10) # Pasar a Binario
print("El numero 10 en binario: ", b)
h = hex(10) # Pasar a Hexadecimal
print("Numero 10 en hexadecimal: ", h)
b = int('0b1010', 2) # Convertir de binario "Base dos" a entero
print("El 10 binario a Entero again: ", b)
h = int('0xa', 16) # Convertir el 10 de hexadecimal a entero. base 16
print("El 10 hexadecimal a Entero again: ", h)
#%% Valor absoluto
absolute = abs(-10)
print(absolute)

absolute2 = abs(10)
print(absolute2)
#%% Redondear
redond = round(5.4)
print("Numero redondeado: 5.4 -> ",redond)
redond2 = round(5.5)
print("Numero redondeado: 5.5 -> ", redond2)
#%% Evaluar
evalu1 = eval("2 + 5")
print(evalu1)
