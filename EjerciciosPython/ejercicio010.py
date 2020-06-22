# Mostrar los archivos de una ruta en especifico.

from os import listdir
from os.path import isfile, join

ruta = r'C:/Users/Santiago/Documents/PROGRAMACION/code4geld/code4geld/EjerciciosPython'

def listar_directorio(ruta):
    """
    Lista el contenido de archivos de un directorio especifico
    """
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a)) ]
    
    return archivos

listar_archivos = listar_directorio(ruta)

print(listar_archivos)
print(len(listar_archivos))