f = open("prueba.txt", "w")
#Crea una línea
f.write("Línea1\n")
f.write("Línea2\n")
#Cierra archivo
f.close()
print("Su archivo ha sido creado")


#LEER ARCHIVO
f = open("prueba.txt","r")
#Se lee el contenido y se guada en la variable
contenido = f.read()
#Se cierra el archivo
f.close()
#Imprimimos con un print usando la variable que contiene la información del archivo
print(contenido)


#AGREGAR
#Se abre el archivo
f = open("prueba.txt", "a")
#Se ingresa la información nueva 
texto = input("Ingrese texto: ")
f.write(texto)
#Se cierra el archivo
f.close()
print("El cambio ha sido guardado")
