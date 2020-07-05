while(True):
    try: # Intenta hacer esto, atrapando un error en bloque de instrucciones
        n = float(input("Introduce un numero: "))
        m = 4
        print("{} / {} = {}".format(n, m, n/m))
    except: # Si ocurre algun error, esta es la excepcion 
        print("Introduce un numero valido. ")
    else: # Si no ocurre ningun error se ejecuta
        print("Todo funciono correctamente.")
        break
    finally: # Finalmente, despues del Try se ejecutara este bloque, haya error o no.
        print("Fin de la iteracion.")

#%%# Multiples excepciones

try:
    n = float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena.")
except Exception as e:
    print( type(e).__name__) # Asi se consigue el tipo del error
    # En e colocamos cualquier abreviatura.
#%%# Invocacion de Excepciones
def mi_funcion(algo = None):
    try:    
        if algo == None:
            raise ValueError("No se permiten valores nulos")
    except ValueError:
        print("Error! No se permite un valor nulo (Desde la excepcion)")

mi_funcion()
