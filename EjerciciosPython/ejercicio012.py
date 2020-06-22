# Acceder a una URL e imprimir su contenido HTML.

from http.client import HTTPConnection

url = "example.com" #Pagina de internet de ejemplo

conexion = HTTPConnection(url)
conexion.request('GET', '/')

#Se escribe 'GET' porque se esta solicitando informacion.
# '/' la barra significa que pedimos informacion de la raiz del sitio web

resultado = conexion.getresponse()
contenido = resultado.read()

print(contenido)