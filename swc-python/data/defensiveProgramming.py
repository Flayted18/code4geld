numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for num in numbers:
    assert num > 0.0, 'Data should only contain positive values'
    total += num
print('total is:', total)
#%%
def normalize_rectangle(rect):
    '''Normaliza un rectángulo para que esté en el origen y con 1.0 unidades de largo en su eje más largo.
     La entrada debe tener el formato (x0, y0, x1, y1).
     (x0, y0) y (x1, y1) definen las esquinas inferior izquierda y superior derecha
     del rectángulo, respectivamente.'''
    assert len(rect) == 4, 'Rectangulos deben contener 4 coordenadas'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)

print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) ))
print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate
print(normalize_rectangle( (4.0, 2.0, 1.0, 5.0) )) # X axis inverted
print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )) # Mas ancho que alto
"""No muestra si los demas errores se cumplen porque el programa se 
detiene al primer error que consigue"""
#Se puede crear tambien una funcion con todos los ASSERT necesarios, y despues solo se hace una llamada.
