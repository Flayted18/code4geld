"""LA FORMULA DE HAVERSINE.

Calcular la distancia entre dos puntos
"""
from math import radians, acos, sin, cos
#%%#Introduciendo las coordenadas y convirtiendolas de Grados decimales a Radianes
#Punto inicial
latini = radians(float(input("Introduzca la Latitud inicial: ")))
print (latini)
lonini = radians(float(input("Introduce la Longitud inicial: ")))
print (lonini)
#Punto final
latfin = radians(float(input("Introduzca la Latitud final: ")))
print (latfin)
lonfin = radians(float(input("Introduce La Longitud final: ")))
print (lonfin)
#%%#Formula para calcular la distancia
r = 6371.01
distancia = r*(acos(sin(latini)*sin(latfin)+cos(latini)*cos(latfin)*cos(lonini-lonfin)))
print ("La distancia entre ambos puntos en Km es de: ",distancia)
