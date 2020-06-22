# Crear una clase para representar los datos de una persona

class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre # self hace el papel del this.x en Javascript
        self.edad = edad
        self.email = email
    
    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nEmail: {}'.format(self.nombre, self.edad, self.email)

Santiago = Persona("Santiago", "20", "correo@gmail.com")

print(Santiago)