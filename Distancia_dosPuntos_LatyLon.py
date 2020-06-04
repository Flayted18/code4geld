"""LA FORMULA DE HAVERSINE.

Calcular la distancia entre dos puntos
"""
import math
#%%#Introduciendo las coordenadas y convirtiendolas de Grados decimales a Radianes
#Punto inicial
latini = math.radians(float(input("Introduzca la Latitud inicial: ")))
print (latini)
lonini = math.radians(float(input("Introduce la Longitud inicial: ")))
print (lonini)
#Punto final
latfin = math.radians(float(input("Introduzca la Latitud final: ")))
print (latfin)
lonfin = math.radians(float(input("Introduce La Longitud final: ")))
print (lonfin)
#%%#Formula para calcular la distancia
r = 6371.01
distancia = r*(math.acos(math.sin(latini)*math.sin(latfin)+math.cos(latini)*math.cos(latfin)*math.cos(lonini-lonfin)))
print ("La distancia entre ambos puntos en Km es de: ",distancia)
