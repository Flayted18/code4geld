#Comprobar si una cadena termina con la extension .py, sino es asi, agragar la extension
# main.py es valido
# modulo no es valido -> modulo.py

def validate_fileName(filename):
    """
    Valida si un nombre de archivo tiene la extension .py, 
    en caso contrario la agrega.
    """
    if len(filename) >= 3 and filename[-3:] == '.py':
        return filename
    else:
        return filename + '.py'

print(validate_fileName("main.py"))
print(validate_fileName("modulo"))