import random #----> Para que el sistema asigne los número de cuenta alazar

"""a = open("BaseDeDatos.txt","w")
a.write("N_Objeto|Nombre|Apellido|dpi|Contraseña|Saldo"+"\n")
a.close()
print("Archivo creado")"""

def menu():
    print(" ________________________")
    print("|       BIENVENIDO       |")
    print("|  AL CAJERO AUTOMÁTICO  |")
    print("|________________________|")    
    print("1. Crear Cuenta")
    print("2. Consulta saldo")
    print("3.Depositar")
    print("4. Retirar")
    print("5.Hacer transferencia a otra cuenta")
    print("6.Olvidé mi número de cuenta")
    print("7.Salir")
    option =input("Ingrese opción: ")
    return option
#DATOS UNIVERSALES

objUsuario = "" #----> Creación de el Objeto Usuario
a = open("BaseDeDatos.txt","r")
Lineas = a.readlines()
ListaDatos =[]
for linea in Lineas:
    linea = linea.replace("\n","").split("|")
    ListaDatos.append(linea)
a.close()

#INICIO DE CLASES
#CLASE PADRE
class Usuario():
    def __init__(self):
        self.nobjeto = ""
        self.nombre = ""
        self.apellido = ""
        self.__dpi = ""
        self.__contraseña = ""
        self.saldo = ""
        self.ncuenta = ""
        self.estado = ""

    #Para crear una cuenta
    def IngresoDatos(self):
        a = open("BaseDeDatos.txt","a+")
        Datos = " " 
        while True:
            self.nobjeto = 0
            self.nombre = input("Ingrese su nombre: ") 
            self.apellido = input("Ingrese apellido: ")
            self.__dpi = input("Ingrese número de DPI: ") #----> Este dato será privado
            self.saldo = input("Ingrese el monto para abrir su cuenta: ")
            self.__contraseña = input("Cree su contraseña: ") #----> Este dato será privado
            self.RepitContraseña= input("Confirme contraseña: ")
            if self.__contraseña != self.RepitContraseña:
                print("La contraseña no coincide, intente nuevamente")
                self.__contraseña = input("Cree su contraseña: ")
                self.RepitContraseña= input("Confirme contraseña: ")
                if self.__contraseña != self.RepitContraseña:
                    print("Error al crear cuenta")
                    print("Las contraseñas no coinciden nuevamente")
                    print("Reinicie su registro")
                    print("Elija la opción Crear cuenta nuevamente")
                    main()
                    break
            self.estado = "Activa"
            if self.estado == "Activa":
                self.ncuenta = random.randint(1000000,9000000)
                print("Felicidades, Has creado tu cuenta")
                print("Tu número de cuenta es: ",self.ncuenta)
                self.nobjeto = self.nobjeto + 1
            Datos += str(self.nobjeto) + "|"
            Datos += self.nombre+ "|"
            Datos += self.apellido+ "|"
            Datos += self.__dpi+ "|"
            Datos += self.__contraseña+ "|"
            Datos += self.saldo + "|"
            Datos += str(self.ncuenta)+ "|"
            Datos += self.estado + "\n"
            break
        
        a.write(Datos)
        a.close()  
        a = open("BaseDeDatos.txt","r")
        Lineas = a.readlines()
        for linea in Lineas:
            linea = linea.replace("\n","").split("|")
            ListaDatos.append(linea)
        a.close

    #Para que el objeto usuario consulte saldo
    def ConsultaS(self):
        Moment= input("Ingrese su número de cuenta:")
        Password = input("Ingrese su contraseña:")
        for linea in ListaDatos:
            if  linea[4] == Password and  linea[6]==Moment:
                print("Bienvenido/a ", linea[1] + " " + linea[2])
                print("Su saldo es: ", linea[5])
            
    #Ya que es necesario ingresar el usuario para hacer movimientos
    #Se hizo esta función para que el objeto usuario recuerde su número de cuenta     
    def rec(self):
        temp = input("Ingrese su contraseña: ")
        for linea in ListaDatos: 
            if linea[4]==temp:
                cuenta = linea[6]
                return cuenta
                   
#CLASE 2: Aquí se definen todos los movimientos monetarios del objeto usuario
#Hereda de la clase usuario
class Movimiento(Usuario):
    def __init__(self):
        self.efectivo=0
        self.transferencia = 0

    #Método para hacer depósitos
    def depositar(self):
        Moment= input("Ingrese su número de cuenta:")
        Password = input("Ingrese su contraseña:")
        for linea in ListaDatos:
            if  linea[4] == Password and  linea[6]==Moment:
                print("Bienvenido/a ", linea[1] + " " + linea[2])
                fila = int(linea[0])
                print(fila)
                cantidad = float(input("Ingrese monto a depositar: "))
                ndata = float(linea[5]) + cantidad
                modificar_dato( [int(fila)], 5, str(ndata))
            a.close()

    #Método para que el objeto usuario retire dinero   
    def debitar(self):
        Moment= input("Ingrese su número de cuenta:")
        Password = input("Ingrese su contraseña:")
        for linea in ListaDatos:
            if  linea[4] == Password and  linea[6]==Moment:
                print("Bienvenido/a ", linea[1] + " " + linea[2])
                fila = int(linea[0])
                print(fila)
                debito = float(input("Ingrese cantidad a retirar: "))
                ndata = float(linea[5]) - debito
                if debito > int(float(linea[5])):
                    print("El saldo en su cuenta es insuficiente")
                else:
                    ndata = float(linea[5]) - debito
                    modificar_dato( [int(fila)], 5, str(ndata))
            
    #Método para que el objeto usuario transfiera dinero a una cuenta del mismo banco
    def Transferir(self):
        Moment= input("Ingrese su número de cuenta:")
        Password = input("Ingrese su contraseña:")
        for linea in ListaDatos:
            if  linea[4] == Password and  linea[6]==Moment:
                cant = 0
                print("Bienvenido/a ", linea[1] + " " + linea[2])
                fila1 = int(linea[0])
                saldo1 = linea[5]
                ncTemp = input("Ingrese número de cuenta para la transferencia: ")
                for linea in ListaDatos:
                    if linea[6] == ncTemp:
                        cant = float(input("Ingrese el monto a transferir: "))
                        fila2 = int(linea[0])
                        ndata2 = float(linea[5]) + cant
                        if cant > int(float(saldo1)):
                            print("El saldo en cuenta es insuficiente")
                        else:
                            modificar_dato( [fila2], 5, str(ndata2))
                            print("Transferencia exitosa")
                    elif linea[6] != ncTemp:
                        print("Lo sentimos, el número de cuenta para la transferencia no existe en nuestra base de datos")
                ndata1 = float(saldo1) - cant
                modificar_dato( [fila1], 5, str(ndata1))

#PROCEDIMIENTO UNIVERSAL
def modificar_dato(filas, columna, nuevo_dato):#----> Este procedimiento es universal ya que es un código reutilizable
        contenido = list()
        a =open("BaseDeDatos.txt", 'r+')
        contenido = a.readlines()
        for fila in filas:
            columnas = contenido[fila-1].split("|")
            columnas[columna] = nuevo_dato
            contenido[fila-1] = '|'.join(columnas)
        a = open("BaseDeDatos.txt","w")
        a.writelines(contenido)
        a.close()

#PROCEDIMIENTOS PARA EL MENÚ
def CreacionCuenta(): #1
    objUsuario = Usuario()
    objUsuario.IngresoDatos()
    print(objUsuario.IngresoDatos())


def Consulta(): #2
    objUsuario.ConsultaS()

def Deposito(): #3
    objUsuario = Movimiento()
    objUsuario.depositar()

def Debito():#4
    objUsuario = Movimiento()
    objUsuario.debitar()

def Transferencia(): #5
    objUsuario=Movimiento()
    objUsuario.Transferir()

def Recordatorio(): #6
    objUsuario = Movimiento()
    print("Su número de cuenta es: ", objUsuario.rec())
    

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            CreacionCuenta()
        elif opcion == "2":
            Consulta()
        elif opcion == "3":
            Deposito()
        elif opcion == "4":
            Debito()
        elif opcion == "5":
            Transferencia()
        elif opcion == "6":
            Recordatorio()
        elif opcion == "7":
            print("El programa ha finalizado")
            break  
        else:
            print("La opción elegida es incorrecta, intente nuevamente")
main()


#Polimorfismo
#encapsulamiento
#abstraccion
#clases
#funciones
#procedimientos









"""def menu():
    print("1. Usuario con cuenta")
    print("2. Crear cuenta")
    print("3.Hacer depósito")
    print("4. Retirar dinero")
    print("5.Consultar saldo")
    print("7.Salir")
    seleccion =input("Ingrese opción: ")
    return seleccion
class opciones:
    option = input(": ")"""



import random
"""a = open("BaseDeDatos.txt","w")
a.write("Nombre|Apellido|dpi|Contraseña|Saldo"+"\n")
a.close()
print("Archivo creado")"""

"""
class CreacionCuenta():
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.dpi = ""
        self.contraseña = ""
        self.saldo = ""
        self.ncuenta = ""
        self.estado = "Inactiva"

    def IngresoDatos(self):
        a = open("BaseDeDatos.txt","a+")
        Datos = " " 
        while True:
            self.nombre = input("Ingrese su nombre: ") 
            self.apellido = input("Ingrese apellido: ")
            self.dpi = input("Ingrese número de DPI: ")
            self.saldo = input("Ingrese el monto para abrir su cuenta: ")
            self.contraseña = input("Cree su contraseña: ")
            self.RepitContraseña= input("Confirme contraseña: ")
            if self.contraseña != self.RepitContraseña:
                print("La contraseña no coincide, intente nuevamente")
                self.contraseña = input("Cree su contraseña: ")
                self.RepitContraseña= input("Confirme contraseña: ")
                if self.contraseña != self.RepitContraseña:
                    print("Error al crear cuenta")
                    print("Las contraseñas no coinciden nuevamente")
                    print("Reinicie su registro")
                    print("Elija la opción Crear cuenta nuevamente")
                    #def menu()
                    break
            self.estado = "Activa"
            if self.estado == "Activa":
                self.ncuenta = random.randint(1000000,9000000)
                print("Felicidades, Has creado tu cuenta")
                print("Tu número de cuenta es: ",self.ncuenta)
            Datos += self.nombre+ "|"
            Datos += self.apellido+ "|"
            Datos += self.dpi+ "|"
            Datos += self.contraseña+ "|"
            Datos += self.saldo + "|"
            Datos += str(self.ncuenta)+ "|"
            Datos += self.estado + "\n"
            break
        
        a.write(Datos)
        a.close()  
        a = open("BaseDeDatos.txt","r")
        Lineas = a.readlines()
        ListaDatos = []
        for linea in Lineas:
            linea = linea.replace("\n","").split("|")
            ListaDatos.append(linea)
            print(ListaDatos)
        a.close






Usuario1 = CreacionCuenta()
Usuario1.IngresoDatos
print(Usuario1.IngresoDatos())"""


"""class Movimiento(CreacionCuenta):
    def __init__(self):
        self.efectivo=""
        self.transferencia = ""

    def eleccion(self):
        a = open("BaseDeDatos.txt","r")
        self.número= input("Ingrese número de cuenta: ")
        self.contraseña = input("Ingrese contraseña: ")
        for i in range(0,len(a)):
            for d in i:
                if d[5] == self.número and d[3] == self.contraseña:
                    print("Bienvenido ", d[0][1])
                else:
                    print("Número de cuenta o Contraseña incorrecta")
                    print("Intente nuevamente")
        a.close()

    def incremento(self,deposito):
        self.ncuenta = input("Ingrese su número de cuenta: ")
        deposito = int(input("Ingrese monto a depositar: "))
        self.saldo = int(self.saldo) + deposito
        a = open("BaseDeDatos.txt","r")
        Lineas = a.readlines()
        L = len(a)
        for i in range(0,L):
            if a[i] == self.número:
                a.close()
                a = open("BaseDeDatos.txt","w")
                a[i] == self.ncuenta
            
Usuario1=Movimiento()
Usuario1.eleccion
print(Usuario1.eleccion)"""
"""
    def debito(self):
        debito = int(input("Ingrese cantidad a retirar: "))
        self.saldo = int(self.saldo) - debito
        if debito > self.saldo:
            print("El saldo en cuenta es insuficiente")
Usuario1 = Movimiento
Usuario1.debito
print(Usuario1.debito())

#Creación de cuenta
Nombre = input("Ingrese nombre: ")
Apellidos = input("Ingrese apellidos: ")
Contraseña = input("Ingrese contraseña")
Saldo = input("Ingrese su depósito: ")

#CREAR ARCHIVO SIN QUE BORRE LA INFORMACIÓN AL EJECUTARLO
import os
#Limpia pantalla
os.system("clear")
#Ingresan el nombre del archivo a crear o cargar
archivo = input("Archivo a crear:")
#Abren archivo para agregar
f = open(archivo,"a+")
#Movemos bytes del archivo al inicio para empezar a leer
f.seek(0)
#Leemos todas las líneas
lineas = f.readlines()
#Imprimimos todas las líneas y anteponemos el símbolo > ya que
#Nuestro editor así muestras las líneas por input que hacemos
for linea in lineas:
    print(">"+linea,end="")
#Empezamos a recolectar el contenido a agregar
contenido = ""
#Ciclo infinito que se rompe al escribir :jeronimo
while True:
    lineaTmp = input(">")
    if lineaTmp == ":jeronimo":
        break
        #Rompe el ciclo
    elif lineaTmp == ":clean":
        #Borra la pantalla
        os.system("clear")
        #Cierra el archivo en modo a+
        f.close()
        #Sobreescribe el archivo en modo w
        f = open(archivo,"w")
        continue
    contenido += lineaTmp+"\n"
#Se escribe el contenido recolectado
#Si se escogio clean se borra el contenido del archivo primero
#agregando a partir de allí nuevas líneas
f.write(contenido)
#Cerramos el archivo
f.close()
#Muestra mensaje que se grabo exitosamente
print("Archivo guardado exitosamente")

def main():
    while True:
         opcion = menu()
         elif opcion == "2":
            IngresoDatos(self)
         elif opcion == "3":
            prom_mes(lista)
         elif opcion == "4":
            maximo_bodega()
         elif opcion == "5":
            Archivo_CSV()
         elif opcion == "6":
            pag_html()
         elif opcion == "7":
            print("El programa ha finalizado")
            break
         else:
            print("La opción elegida es incorrecta, intente nuevamente")
main()"""

import random  #----> Para que el sistema asigne los número de cuenta alazar
"""a = open("BaseDeDatos.txt","w")
a.write("N_Objeto|Nombre|Apellido|dpi|Contraseña|Saldo"+"\n")
a.close()
print("Archivo creado")"""


def menu():
	print(" ________________________")
	print("|       BIENVENIDO       |")
	print("|  AL CAJERO AUTOMÁTICO  |")
	print("|________________________|")
	print("1. Crear Cuenta")
	print("2. Consulta saldo")
	print("3.Depositar")
	print("4. Retirar")
	print("5.Hacer transferencia a otra cuenta")
	print("6.Olvidé mi número de cuenta")
	print("7.Salir")
	option = input("Ingrese opción: ")
	return option


#DATOS UNIVERSALES

objUsuario = ""  #----> Creación de el Objeto Usuario
a = open("BaseDeDatos.txt", "r")
Lineas = a.readlines()
ListaDatos = []
for linea in Lineas:
	linea = linea.replace("\n", "").split("|")
	ListaDatos.append(linea)
a.close()


#INICIO DE CLASES
#CLASE PADRE
class Usuario():
	def __init__(self):
		self.nobjeto = ""
		self.nombre = ""
		self.apellido = ""
		self.__dpi = ""
		self.__contraseña = ""
		self.saldo = ""
		self.ncuenta = ""
		self.estado = ""

	#Para crear una cuenta
	def IngresoDatos(self):
		a = open("BaseDeDatos.txt", "a+")
		Datos = " "
		while True:
			self.nobjeto = 0
			self.nombre = input("Ingrese su nombre: ")
			self.apellido = input("Ingrese apellido: ")
			self.__dpi = input(
			    "Ingrese número de DPI: ")  #----> Este dato será privado
			self.saldo = input("Ingrese el monto para abrir su cuenta: ")
			self.__contraseña = input(
			    "Cree su contraseña: ")  #----> Este dato será privado
			self.RepitContraseña = input("Confirme contraseña: ")
			if self.__contraseña != self.RepitContraseña:
				print("La contraseña no coincide, intente nuevamente")
				self.__contraseña = input("Cree su contraseña: ")
				self.RepitContraseña = input("Confirme contraseña: ")
				if self.__contraseña != self.RepitContraseña:
					print("Error al crear cuenta")
					print("Las contraseñas no coinciden nuevamente")
					print("Reinicie su registro")
					print("Elija la opción Crear cuenta nuevamente")
					main()
					break
			self.estado = "Activa"
			if self.estado == "Activa":
				self.ncuenta = random.randint(1000000, 9000000)
				print("Felicidades, Has creado tu cuenta")
				print("Tu número de cuenta es: ", self.ncuenta)
				self.nobjeto = self.nobjeto + 1
			Datos += str(self.nobjeto) + "|"
			Datos += self.nombre + "|"
			Datos += self.apellido + "|"
			Datos += self.__dpi + "|"
			Datos += self.__contraseña + "|"
			Datos += self.saldo + "|"
			Datos += str(self.ncuenta) + "|"
			Datos += self.estado + "\n"
			break

		a.write(Datos)
		a.close()
		a = open("BaseDeDatos.txt", "r")
		Lineas = a.readlines()
		for linea in Lineas:
			linea = linea.replace("\n", "").split("|")
			ListaDatos.append(linea)
		a.close

	#Para que el objeto usuario consulte saldo
	def ConsultaS(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				print("Su saldo es: ", linea[5])

	#Ya que es necesario ingresar el usuario para hacer movimientos
	#Se hizo esta función para que el objeto usuario recuerde su número de cuenta
	def rec(self):
		temp = input("Ingrese su contraseña: ")
		for linea in ListaDatos:
			if linea[4] == temp:
				cuenta = linea[6]
				return cuenta


#CLASE 2: Aquí se definen todos los movimientos monetarios del objeto usuario
#Hereda de la clase usuario
class Movimiento(Usuario):
	def __init__(self):
		self.efectivo = 0
		self.transferencia = 0

	#Método para hacer depósitos
	def depositar(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				print(fila)
				cantidad = float(input("Ingrese monto a depositar: "))
				ndata = float(linea[5]) + cantidad
				modificar_dato([int(fila)], 5, str(ndata))
			a.close()

	#Método para que el objeto usuario retire dinero
	def debitar(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				print(fila)
				debito = float(input("Ingrese cantidad a retirar: "))
				ndata = float(linea[5]) - debito
				if debito > int(float(linea[5])):
					print("El saldo en su cuenta es insuficiente")
				else:
					ndata = float(linea[5]) - debito
					modificar_dato([int(fila)], 5, str(ndata))

	#Método para que el objeto usuario transfiera dinero a una cuenta del mismo banco
	def Transferir(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				cant = 0
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila1 = int(linea[0])
				saldo1 = linea[5]
				ncTemp = input(
				    "Ingrese número de cuenta para la transferencia: ")
				for linea in ListaDatos:
					if linea[6] == ncTemp:
						cant = float(input("Ingrese el monto a transferir: "))
						fila2 = int(linea[0])
						ndata2 = float(linea[5]) + cant
						if cant > int(float(saldo1)):
							print("El saldo en cuenta es insuficiente")
						else:
							modificar_dato([fila2], 5, str(ndata2))
							print("Transferencia exitosa")
					elif linea[6] != ncTemp:
						print(
						    "Lo sentimos, el número de cuenta para la transferencia no existe en nuestra base de datos"
						)
				ndata1 = float(saldo1) - cant
				modificar_dato([fila1], 5, str(ndata1))


#PROCEDIMIENTO UNIVERSAL
def modificar_dato(
    filas, columna, nuevo_dato
):  #----> Este procedimiento es universal ya que es un código reutilizable
	contenido = list()
	a = open("BaseDeDatos.txt", 'r+')
	contenido = a.readlines()
	for fila in filas:
		columnas = contenido[fila - 1].split("|")
		columnas[columna] = nuevo_dato
		contenido[fila - 1] = '|'.join(columnas)
	a = open("BaseDeDatos.txt", "w")
	a.writelines(contenido)
	a.close()


#PROCEDIMIENTOS PARA EL MENÚ
def CreacionCuenta():  #1
	objUsuario = Usuario()
	objUsuario.IngresoDatos()
	print(objUsuario.IngresoDatos())


def Consulta():  #2
	objUsuario.ConsultaS()


def Deposito():  #3
	objUsuario = Movimiento()
	objUsuario.depositar()


def Debito():  #4
	objUsuario = Movimiento()
	objUsuario.debitar()


def Transferencia():  #5
	objUsuario = Movimiento()
	objUsuario.Transferir()


def Recordatorio():  #6
	objUsuario = Movimiento()
	print("Su número de cuenta es: ", objUsuario.rec())


def main():
	while True:
		opcion = menu()
		if opcion == "1":
			CreacionCuenta()
		elif opcion == "2":
			Consulta()
		elif opcion == "3":
			Deposito()
		elif opcion == "4":
			Debito()
		elif opcion == "5":
			Transferencia()
		elif opcion == "6":
			Recordatorio()
		elif opcion == "7":
			print("El programa ha finalizado")
			break
		else:
			print("La opción elegida es incorrecta, intente nuevamente")


main()




import random  #----> Para que el sistema asigne los número de cuenta alazar
"""a = open("BaseDeDatos.txt","w")
a.write("N_Objeto|Nombre|Apellido|dpi|Contraseña|Saldo"+"\n")
a.close()
print("Archivo creado")"""


def menu():
	print(" ________________________")
	print("|       BIENVENIDO       |")
	print("|  AL CAJERO AUTOMÁTICO  |")
	print("|________________________|")
	print("1. Crear Cuenta")
	print("2. Consulta saldo")
	print("3.Depositar")
	print("4. Retirar")
	print("5.Hacer transferencia a otra cuenta")
	print("6.Olvidé mi número de cuenta")
	print("7.Salir")
	option = input("Ingrese opción: ")
	return option


#DATOS UNIVERSALES

objUsuario = ""  #----> Creación de el Objeto Usuario
a = open("BaseDeDatos.txt", "r")
Lineas = a.readlines()
ListaDatos = []
for linea in Lineas:
	linea = linea.replace("\n", "").split("|")
	ListaDatos.append(linea)
a.close()


#INICIO DE CLASES
#CLASE PADRE
class Usuario():
	def __init__(self):
		self.nobjeto = ""
		self.nombre = ""
		self.apellido = ""
		self.__dpi = ""
		self.__contraseña = ""
		self.saldo = ""
		self.ncuenta = ""
		self.estado = ""

	#Para crear una cuenta
	def IngresoDatos(self):
		a = open("BaseDeDatos.txt", "a+")
		Datos = " "
		while True:
			self.nobjeto = 0
			self.nombre = input("Ingrese su nombre: ")
			self.apellido = input("Ingrese apellido: ")
			self.__dpi = input(
			    "Ingrese número de DPI: ")  #----> Este dato será privado
			self.saldo = input("Ingrese el monto para abrir su cuenta: ")
			self.__contraseña = input(
			    "Cree su contraseña: ")  #----> Este dato será privado
			self.RepitContraseña = input("Confirme contraseña: ")
			if self.__contraseña != self.RepitContraseña:
				print("La contraseña no coincide, intente nuevamente")
				self.__contraseña = input("Cree su contraseña: ")
				self.RepitContraseña = input("Confirme contraseña: ")
				if self.__contraseña != self.RepitContraseña:
					print("Error al crear cuenta")
					print("Las contraseñas no coinciden nuevamente")
					print("Reinicie su registro")
					print("Elija la opción Crear cuenta nuevamente")
					main()
					break
			self.estado = "Activa"
			if self.estado == "Activa":
				self.ncuenta = random.randint(1000000, 9000000)
				print("Felicidades, Has creado tu cuenta")
				print("Tu número de cuenta es: ", self.ncuenta)

			lectura = open("BaseDeDatos.txt", "r")
			lectura.readline()
			lectura.seek(0)

			self.nobjeto = len(lectura.readlines()) + 1
			
			Datos += str(self.nobjeto) + "|"
			Datos += self.nombre + "|"
			Datos += self.apellido + "|"
			Datos += self.__dpi + "|"
			Datos += self.__contraseña + "|"
			Datos += self.saldo + "|"
			Datos += str(self.ncuenta) + "|"
			Datos += self.estado + "\n"
			break

		a.write(Datos)
		a.close()
		a = open("BaseDeDatos.txt", "r")
		Lineas = a.readlines()
		for linea in Lineas:
			linea = linea.replace("\n", "").split("|")
			ListaDatos.append(linea)
		a.close
		

	#Para que el objeto usuario consulte saldo
	def ConsultaS(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				print("Su saldo es: ", linea[5])

	#Ya que es necesario ingresar el usuario para hacer movimientos
	#Se hizo esta función para que el objeto usuario recuerde su número de cuenta
	def rec(self):
		temp = input("Ingrese su contraseña: ")
		for linea in ListaDatos:
			if linea[4] == temp:
				cuenta = linea[6]
				return cuenta


#CLASE 2: Aquí se definen todos los movimientos monetarios del objeto usuario
#Hereda de la clase usuario
class Movimiento(Usuario):
	def __init__(self):
		self.efectivo = 0
		self.transferencia = 0

	#Método para hacer depósitos
	def depositar(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				print(fila)
				cantidad = float(input("Ingrese monto a depositar: "))
				ndata = float(linea[5]) + cantidad
				modificar_dato([int(fila)], 5, str(ndata))
				a.close()

	#Método para que el objeto usuario retire dinero
	def debitar(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				print(fila)
				debito = float(input("Ingrese cantidad a retirar: "))
				if debito < int(float(linea[5])):
					ndata_db = float(linea[5]) - debito
					modificar_dato([int(fila)], 5, str(ndata_db))
					a.close()
				elif debito > int(float(linea[5])):
					print("El saldo en su cuenta es insuficiente")
				

	#Método para que el objeto usuario transfiera dinero a una cuenta del mismo banco
	def Transferir(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		for linea in ListaDatos:
			if linea[4] == Password and linea[6] == Moment:
				cant = 0
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila1 = int(linea[0])
				saldo1 = linea[5]
				ncTemp = input(
				    "Ingrese número de cuenta para la transferencia: ")
				for linea in ListaDatos:
					if linea[6] == ncTemp:
						cant = float(input("Ingrese el monto a transferir: "))
						fila2 = int(linea[0])
						ndata2 = float(linea[5]) + cant
						if cant > int(float(saldo1)):
							print("El saldo en cuenta es insuficiente")
						else:
							modificar_dato([fila2], 5, str(ndata2))
							print("Transferencia exitosa")
					elif linea[6] != ncTemp:
						print(
						    "Lo sentimos, el número de cuenta para la transferencia no existe en nuestra base de datos"
						)
				ndata1 = float(saldo1) - cant
				modificar_dato([fila1], 5, str(ndata1))


#PROCEDIMIENTO UNIVERSAL
def modificar_dato(
    filas, columna, nuevo_dato
):  #----> Este procedimiento es universal ya que es un código reutilizable
	contenido = list()
	a = open("BaseDeDatos.txt", 'r+')
	contenido = a.readlines()
	for fila in filas:
		columnas = contenido[fila - 1].split("|")
		columnas[columna] = nuevo_dato
		contenido[fila - 1] = '|'.join(columnas)
	a = open("BaseDeDatos.txt", "w")
	a.writelines(contenido)
	a.close()


#PROCEDIMIENTOS PARA EL MENÚ
def CreacionCuenta():  #1
	objUsuario = Usuario()
	objUsuario.IngresoDatos()


def Consulta():  #2
    objUsuario= Usuario()
    objUsuario.ConsultaS()


def Deposito():  #3
	objUsuario = Movimiento()
	objUsuario.depositar()


def Debito():  #4
	objUsuario = Movimiento()
	objUsuario.debitar()


def Transferencia():  #5
	objUsuario = Movimiento()
	objUsuario.Transferir()


def Recordatorio():  #6
	objUsuario = Movimiento()
	print("Su número de cuenta es: ", objUsuario.rec())


def main():
	while True:
		opcion = menu()
		if opcion == "1":
			CreacionCuenta()
		elif opcion == "2":
			Consulta()
		elif opcion == "3":
			Deposito()
		elif opcion == "4":
			Debito()
		elif opcion == "5":
			Transferencia()
		elif opcion == "6":
			Recordatorio()
		elif opcion == "7":
			print("El programa ha finalizado")
			break
		else:
			print("La opción elegida es incorrecta, intente nuevamente")


main()




def ingreso():
        def registro(self):
        a = open("Jugadores.txt", "a+")
        Datos = ""
        lista = []
        nombre = ""
        while True:
            nombre = input("Ingrese nombre: ")
            nacionalidad = input("Ingrese su nacionalidad: ")
            apodo = input("Ingrese su apodo: ")
            edad = input("Ingrese su edad: ")
            puntajes = 0
            niveles = 0
            contraseña = input("Cree su contraseña: ")
            repit_contraseña = input("Confirme su contraseña: ")
            if contraseña != repit_contraseña:
                print("La contraseña no coincide, intente nuevamente")
                contraseña = input("Cree su contraseña: ")
                repit_contraseña = input("Confirme su contraseña: ")
                if contraseña != repit_contraseña:
                    print("Error al crear cuenta")
                    print("Las contraseñas no coinciden nuevamente")
                    print("Reinicie su registro")
                    print("Elija la opción Crear cuenta nuevamente")
            estado = "Activa"
            jugador 
            Datos += nombre + "|"
            Datos += apodo + "|"
            Datos += nacionalidad + "|"
            Datos += edad + "|"
            Datos += contraseña + "|"
            Datos += estado + "|"
            Datos += str(puntajes) + "|"
            Datos += str(niveles) + "\n"
            break

        a.write(Datos)
        a.close()
        a = open("Jugadores.txt", "r")
        Lineas = a.readlines()
        for linea in Lineas:
            linea = linea.replace("\n", "").split("|")
            lista.append(linea)
        a.close
		

jugador = Jugadores()
jugador.registro()

