class Pelicula:
    # constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula', self.titulo)
        
    # destructor de clase
    def __del__(self):
        print('Se esta borrando la pelicula')
        
    # redefinimos el metodo String
    def __str__(self):
        return "{} lanzada en {} con una duracion de {}".format(self.titulo, self.lanzamiento, self.duracion)
    
    # redefinir metodo Length
    def __len__(self):
        return self.duracion
        
p = Pelicula('El Padrino', 175, 1972)
del(p) #Borrando el objeto.


