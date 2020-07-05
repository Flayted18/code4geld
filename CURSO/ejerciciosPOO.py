# SuperClass Vehiculo
class Vehiculo():
    def __init__(self, color = None, ruedas = None):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return ("Color {} y {} ruedas.".format(self.color, self.ruedas))
        
    
# SubClase de Vehiculo -> Coche
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return "El coche es de color {}, tiene {} ruedas, velocidad maxima de {} y {} cilindros".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

# SubClase de Coche -> Camioneta
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ". Permite {} carga.".format(self.carga)
    
# SubClase de Vehiculo -> Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        # try: # Intento de validar el tipo del vehiculo! No funciono
        #     if(tipo == "Urbano" or tipo == "Deportiva"):
        #        self.tipo = tipo
        # except:
        #     self.tipo = None
        #     print("El tipo es incorrecto")
        
    def __str__(self):
        return "La bicicleta es de color {}, tiene {} ruedas y es de tipo {}".format(self.color, self.ruedas, self.tipo)

# SubClase de Bicicleta -> Motocicleta
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + "Alcanza una velocidad de {} y tiene {} cilindros.".format(self.velocidad, self.cilindrada)

vehiculos = [
    Coche("Rojo", 4, "160 Km/h", 4),
    Camioneta("Azul", 6, "180 Km/h", 8, "500 Kg"),
    Bicicleta("Naranja", 2, "Urbana"),
    Motocicleta("Negro con franjas amarillas", 2, "Urbano", "220 Km/h", 2)
]

def catalogar(lista):
    for v in lista:
        print("{}. {}".format( type(v).__name__, v ))
        
catalogar(vehiculos)





