# Comprobar si un caracter dado es una vocal.

def is_vowel(c):
    """
    Comprueba si el caracter ingresado es una vocal
    """
    if len(c) == 1:
        vowels = 'aeiou'
        c = c.lower()
        return c in vowels
    else:
        return False
        

print(is_vowel("i"))
print(is_vowel("I"))
print(is_vowel("z"))
print(is_vowel("ae")) 