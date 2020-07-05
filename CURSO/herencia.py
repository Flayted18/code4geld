import copy
# SuperClase Producto
class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    
    # Redefiniendo el String por defecto
    def __str__(self):
        return """\
REFERENCIA \t\t{}
NOMBRE \t\t\t{}
PVP \t\t\t{}
DESCRIPCION \t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion)

# Clase Adorno
class Adorno(Producto):
    pass

# Clase Alimento
class Alimento(Producto):
    productor = ''
    distribuidor = ''
    
    # Redefiniendo el String por defecto
    def __str__(self):
        return """\
REFERENCIA \t\t{}
NOMBRE \t\t\t{}
PVP \t\t\t{}
DESCRIPCION \t{}
PRODUCTOR\t\t{}
DISTRIBUIDOR\t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor,self.distribuidor)

# Clase Libro
class Libro(Producto):
    isbn = ""
    autor = ""
    # Redefiniendo el String por defecto
    def __str__(self):
        return """\
REFERENCIA \t\t{}
NOMBRE \t\t\t{}
PVP \t\t\t{}
DESCRIPCION \t{}
ISBN\t\t\t{}
AUTOR\t\t\t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion,self.isbn, self.autor)
#%%
# Creando Objetos.
adorno = Adorno(2034, 'Vaso Adornado', 15, 'Vaso de porcelana con dibujos')
# print(adorno)
# print("------------------------")

alimento = Alimento(2035, 'Botella de Aceite de Oliva Extra', 5, '250 ml')
alimento.productor = 'La Aceitera'
alimento.distribuidor = 'Distribuciones SA'
# print(alimento)
# print("------------------------")

libro = Libro(2036, 'Cocina Mediterranea', 9, "Recetas Sanas")
libro.isbn = "0-123456-78-9"
libro.autor = 'Donia Juana'
libro2 = Libro(2036, 'El Quijote', 9, "Accion")
libro2.isbn = "0-184456-78-9"
libro2.autor = 'Cervantes'
# print(libro)
# print("------------------------")
# print("------------------------")
# print(" ")

productos = [adorno, alimento]
productos.append(libro)
productos.append(libro2)

for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia,"-", p.nombre)
    elif( isinstance(p, Alimento)):
        print(p.referencia,"-", p.nombre,". ",p.productor)
    elif(isinstance(p, Libro)):
        print(p.referencia,"-", p.nombre,". ", p.isbn)
        
print("------------------------")
def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio"""
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

alimento_rebajado = copy.copy(alimento)
rebajar_producto(alimento_rebajado, 10)
print("COPIA CON REBAJA\n", alimento_rebajado)
print("ORIGINAL\n",alimento)
        

       
    
