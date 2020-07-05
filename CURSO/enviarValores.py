#%%
def suma(a, b):
    return a + b

r = suma(2, 8)

print(r)
#%% Argumentos por valor y referencia

def doblar_valor(numero):
    return numero * 2
    
n = 10
n = doblar_valor(n)
print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns)
print(ns)
#%%# Argumentos indeterminados
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",1,2,3,4,5)

print("")

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, ": ", kwargs[kwarg])

indeterminados_nombre(c = 5, t = "Hola", l = [1,2,3,4,5])

print(" ")
#%%
def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("Sumatorio indeterminado:", t)
    for kwarg in kwargs:
        print(kwarg, ": ", kwargs[kwarg])
        
super_funcion(10, 50, -1, 1.56, nombre = "Santiago", edad = 27)
    
