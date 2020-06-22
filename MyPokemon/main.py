from constants import *
from models import *

# Definimos los Pokemon.

pokemon1 = Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

# Stats

pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
    }

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
    }

# Attacks

pokemon1.attacks = [Attack("Scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("Scratch", "normal", PHYSICAL, 10, 10, 100)]
    
