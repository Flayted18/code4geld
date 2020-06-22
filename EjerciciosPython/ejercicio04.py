# Simular el funcionamiento del operador in.

def pertenece_a(lista, elemento):
    """
    Comprueba si un elemento esta disponile en una lista
    """
    for e in lista:
        if elemento == e:
            return True
    
    return False

print("1: ", pertenece_a([2, 7, 5, 9, 11], 5))
print("2: ", pertenece_a([2, 7, 5, 9, 11], 19))
print("3: ", pertenece_a("Cadena de Texto", "c")) # c pasa por False porque esta en Minuscula
print("4: ", pertenece_a("Cadena de Texto", "C"))
print("5: ", pertenece_a("Cadena de Texto", "k"))