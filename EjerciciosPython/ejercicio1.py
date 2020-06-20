# Calcular la diferencia en Dias de Dos fechas dadas

from datetime import date

hoy = date(2020, 6, 20)
otra_fecha = date(2020, 7, 12)

delta = otra_fecha - hoy

print(delta)
print(delta.days)