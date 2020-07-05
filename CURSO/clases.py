class Galleta:
    chocolate = False
    def __init__(self, sabor = None, forma = None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {} ".format(sabor, forma))
    
    def chocolatear(self):
        self.chocolate = True
    
    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta chocolateada :D ")
        else:
            print("Soy una galleta sin chocolate :C ")
        
            
            
g = Galleta('salada', 'cuadrada')
g.chocolatear()
print(g.tiene_chocolate())