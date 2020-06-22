# Creando jerarquias de Herencia BASICA.

class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
    
class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera
    
Andres = Estudiante("123", "Andres", "correoAndres@gmail.com", "17183", "Contaduria")

print(isinstance(Andres, Estudiante))
print(isinstance(Andres, Persona))
