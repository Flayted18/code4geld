class Battle:
    
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0
        
    def is_finished(self):
        return self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0
    
        



class Pokemon:
    
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.current_status = 0 # Envenenado, paralizado, etc
        self.current_hp = 0 # Vida actual
        self.stats = {} # Estadisticas internas del Pokemon
        self.attacks = {} # Vector de ataques.

class Attack:
    
    def __init__(self, name, typeA, category, pp, power,  accuracy):
        self.name = name
        self.typeA = typeA
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        