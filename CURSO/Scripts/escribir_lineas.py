import sys

if len(sys.argv) == 3:
    
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce correctamente los argumentos.")
    print("Ejemplo: filename.py - 'Texto' - repeticiones")

