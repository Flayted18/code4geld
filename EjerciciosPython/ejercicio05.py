# Generar un conjunto de numeros aleatorios y determinar cuales son impares.

from random import randint
randNum = [randint(1, 100) for _ in range(50)]

print(randNum)

impares = filter(lambda n: n % 2 == 1, randNum)
print()

print("Imprimiendo con lista: ", list(impares))

print()

def findImpar(lista):
    numImpar = []
    
    for n in lista:
        
        if n % 2 == 1:
            numImpar.append(n)         
            
    return numImpar

print("Haciendo una funcion: ", findImpar(randNum))