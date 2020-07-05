#%%
def test():
    return "Una cadena retornada"
print(test())

#%%
def lista():
    return [1,2,3,4,5]
print(lista())
print(" ")
print(lista()[1:4])
#%%
def mix():
    return "Una cadena",20,[1,2,3]

print(mix())
print("------")
c, n, l = mix()
print(c)
print(n)
print(l)