

archivo = open('Archivo.txt', 'w')
archivo.write("Modificación de texto")
archivo.close()

archivo = open('Archivo.txt', 'r')
contenido = archivo.read()
archivo.close()
print(contenido)
