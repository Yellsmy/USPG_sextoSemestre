
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
		continuar()
		
		

	#Para que el objeto usuario consulte saldo
	def ConsultaS(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		a = open("BaseDeDatos.txt","r")
		lineas = a.readlines()
		for linea in lineas:
			linea = linea.replace("\n", "").split("|")
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				print("Su saldo es: ", linea[5])
		a.close()
		continuar()
		

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
		a = open("BaseDeDatos.txt","r")
		lineas = a.readlines()
		
		for linea in lineas:
			linea = linea.replace("\n", "").split("|")
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				cantidad = float(input("Ingrese monto a depositar: "))
				ndata = float(linea[5]) + cantidad
				modificar_dato([int(fila)], 5, str(ndata))
		a.close()
		continuar()
		

	#Método para que el objeto usuario retire dinero
	def debitar(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		a = open("BaseDeDatos.txt","r")
		lineas = a.readlines()
		for linea in lineas:
			linea = linea.replace("\n", "").split("|")
			if linea[4] == Password and linea[6] == Moment:
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila = int(linea[0])
				debito = float(input("Ingrese cantidad a retirar: "))
				if debito < int(float(linea[5])):
					ndata_db = float(linea[5]) - debito
					modificar_dato([int(fila)], 5, str(ndata_db))
				elif debito > int(float(linea[5])):
					print("El saldo en su cuenta es insuficiente")
		a.close()
		continuar()
		

	#Método para que el objeto usuario transfiera dinero a una cuenta del mismo banco
	def Transferir(self):
		Moment = input("Ingrese su número de cuenta:")
		Password = input("Ingrese su contraseña:")
		a = open("BaseDeDatos.txt","r")
		lineas = a.readlines()
		for linea in lineas:
			linea = linea.replace("\n", "").split("|")
			if linea[4] == Password and linea[6] == Moment:
				cant = 0
				print("Bienvenido/a ", linea[1] + " " + linea[2])
				fila1 = int(linea[0])
				saldo1 = linea[5]
				ncTemp = input(
				    "Ingrese número de cuenta para la transferencia: ")
				for linea in lineas:
					linea = linea.replace("\n", "").split("|")
					if linea[6] == ncTemp:
						cant = float(input("Ingrese el monto a transferir: "))
						fila2 = int(linea[0])
						ndata2 = float(linea[5]) + cant
						if cant > int(float(saldo1)):
							print("El saldo en cuenta es insuficiente")
						else:
							modificar_dato([fila2], 5, str(ndata2))
							print("Transferencia exitosa")
				ndata1 = float(saldo1) - cant
				modificar_dato([fila1], 5, str(ndata1))
		a.close()
		continuar()
		
		

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

def continuar():
	selection = input("¿Desea hacer otro movimiento? si  no: ")
	while True:
		if selection == "SI" or selection == "Si" or selection == "si" or selection == "sí":
			main()
		elif selection == "NO" or selection == "No" or selection == "no" :
			print("Gracias por utilizar nuestro servicio")
			opcion = 7
			break
		else:
			print("Su respuesta es inválida")
			print("Escriba si o no")

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
	continuar()


#PROCEDIMIENTO MENÚ
def main():
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
	else:
		print("La opción elegida es incorrecta, intente nuevamente")
		main()

main()
