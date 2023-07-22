import json
def Creacion():
    data = {}
    data["jugadores"] = []
    data ["jugadores"].append({
                "nombre" :"Prueba", 
                "nacionalidad" :"Guatemalteca",
                "apodo" : "Prueba1",
                "edad" : "24",
                "estado" : "Inactiva"})
    with open("BaseDeDatosJ.json", "w") as file:
        json.dump(data, file, indent=5)  
    

class Jugadores():
    def __init__(self):
        nombre = " "
        nacionalidad = ""
        apodo = ""
        edad = 0
        puntajes = 0
        niveles = 0
        contraseña = ""
        estado = ""
        
    def cargarUsuario(self,nombre, contraseña, nacionalidad, edad, apodo, estado):
        try:
            self.nombre = nombre
            self.contraseña = contraseña
            self.nacionalidad = nacionalidad
            self.apodo = apodo
            self.edad = edad
            self.estado = estado
        except TabError:
            print("Error de tabulación")

    def registro(self):
        #try: 
            BaseDatos = open("BaseDeDatosJ.json", "r")
            datos = json.load(BaseDatos)
            BaseDatos.close()
            while True:
                try:
                    IntentosA = 3
                    print(IntentosA)
                    IntentosC = 3
                    estado = "Activa"
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese su edad: "))
                    if edad <= 6:
                        print("Lo sentimos, debes ser mayor de 6 años para registrarte")
                        print("Si has cometido un error al ingresar tu edad, intenta nuevamente")
                        edad = int(input("Ingrese su edad: "))
                        if edad <= 6:
                            print("Lo sentimos, debes ser mayor de 6 años para registrarte")
                            break
                    nacionalidad = input("Ingrese su nacionalidad: ")
                    print(IntentosA)
                    while IntentosA > 0:
                        print(IntentosA)
                        apodo = input("Ingrese su apodo: ")
                        for j in datos["jugadores"]:
                            if j["apodo"] == apodo:
                                print(IntentosA)
                                print("Lo sentimos, el apodo", apodo, "ya está en uso")
                                print("Intente nuevamente, tiene", IntentosA, "intentos más")
                                IntentosA = IntentosA - 1
                            elif j["apodo"] != apodo:
                                IntentosA = 0
                    
                    while IntentosC > 0:
                        contraseña = input("Cree su contraseña: ")
                        repit_contraseña = input("Confirme su contraseña: ")
                        if contraseña != repit_contraseña:
                            print("La contraseña no coincide, intente nuevamente")
                            IntentosC -= 1
                        elif contraseña == repit_contraseña:
                                IntentosC = 0
                    x = {
                    "nombre" :nombre, 
                    "nacionalidad" : nacionalidad,
                    "apodo" : apodo,
                    "edad" : edad,
                    "estado" : estado}
                    with open("BaseDeDatosJ.json") as file:
                        datos = json.load(file)
                        datos["jugadores"].append(x)
                    with open("BaseDeDatosJ.json", "w") as file:
                        json.dump(datos, file, indent=5)
                    break
                except ValueError:
                    print("Error, su edad debe ser en números y no en letras, inténtelo nuevamente")


            """a.write(Datos)
            a.close()
            a = open("Jugadores.txt", "r")
            Lineas = a.readlines()
            for linea in Lineas:
                linea = linea.replace("\n", "").split("|")
                lista.append(linea)
            a.close
        except FileNotFoundError:
            print("Archivo no existe")"""
		
jugador = Jugadores()
jugador.registro()



"""import json
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
def Creacion():
    data = {}
    data["jugadores"] = []
    data ["jugadores"].append({
                "nombre" :"Prueba", 
                "nacionalidad" :"Guatemalteca",
                "apodo" : "Prueba1",
                "edad" : "24",
                "estado" : "Inactiva"})
    with open("BaseDeDatosJ.json", "w") as file:
        json.dump(data, file, indent=5)  
    

class Jugadores():
    def __init__(self):
        nombre = " "
        nacionalidad = ""
        apodo = ""
        edad = 0
        puntajes = 0
        niveles = 0
        contraseña = ""
        estado = ""
        
    def cargarUsuario(self,nombre, contraseña, nacionalidad, edad, apodo, estado):
        try:
            self.nombre = nombre
            self.contraseña = contraseña
            self.nacionalidad = nacionalidad
            self.apodo = apodo
            self.edad = edad
            self.estado = estado
        except TabError:
            print("Error de tabulación")

    def registro(self):
            BaseDatos = open("BaseDeDatosJ.json", "r")
            datos = json.load(BaseDatos)
            BaseDatos.close()
            for j in datos["jugadores"]:
                Ap = j["apodo"]
            while True:
                try:
                    estado = "Activa"
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese su edad: "))
                    if edad <= 6:
                        print("Lo sentimos, debes ser mayor de 6 años para registrarte")
                        print("Si has cometido un error al ingresar tu edad, intenta nuevamente")
                        edad = int(input("Ingrese su edad: "))
                        if edad <= 6:
                            print("Lo sentimos, debes ser mayor de 6 años para registrarte")
                            break
                    nacionalidad = input("Ingrese su nacionalidad: ")
                    apodo = input("Ingrese su apodo: ")
                    if apodo == Ap:
                        while True:
                            print("Lo sentimos, el apodo", apodo, "ya está en uso")
                            print("Intente nuevamente")
                            apodo = input("Ingrese su apodo: ")
                            if apodo != Ap:
                                break 
                    contraseña = input("Cree su contraseña: ")
                    repit_contraseña = input("Confirme su contraseña: ")
                    if contraseña != repit_contraseña:
                        while True:
                            print("La contraseña no coincide, intente nuevamente")
                            contraseña = input("Cree su contraseña: ")
                            repit_contraseña = input("Confirme su contraseña: ")
                            if contraseña == repit_contraseña:
                                break
                    x = {
                    "nombre" :nombre,
                    "Contraseña" : contraseña, 
                    "nacionalidad" : nacionalidad,
                    "apodo" : apodo,
                    "edad" : edad,
                    "estado" : estado}
                    with open("BaseDeDatosJ.json") as file:
                        datos = json.load(file)
                        datos["jugadores"].append(x)
                    with open("BaseDeDatosJ.json", "w") as file:
                        json.dump(datos, file, indent=6)
                    print(" ________________________")
                    print("|     ¡¡FELICIDADES!!    |")
                    print("|  HAS CREADO TU CUENTA  |")
                    print("|________________________|")
                    self.cargarUsuario(nombre, nacionalidad, contraseña, apodo, edad,estado)
                    break
                except ValueError:
                    print("Error, su edad debe ser en números y no en letras, inténtelo nuevamente")

    
		
jugador = Jugadores()
jugador.registro()



def modificar(archivo, antiguo_dato, nuevo_dato):
    #Crear linea temporal
    Antiguo, Nuevo = mkstemp()
    with fdopen(Antiguo,'w') as nueva_fila:
        with open(archivo) as vieja_linea:
            for linea in vieja_linea:
                nueva_fila.write(linea.replace(antiguo_dato, nuevo_dato))
    #Remover linea antigua
    remove(archivo)
    #Insertar nuevo dato
    move(Nuevo, archivo)

def menu2():
    print("¿Qué dato quieres modificar?")
    print("1.Nombre")
    print("2.Contraseña")
    print("3.Apodo")
    print("4. Edad")


with open("BaseDeDatosJ.json") as f:
    data = json.load(f)
BaseDatos = open("BaseDeDatosJ.json", "r")
datos = json.load(BaseDatos)
BaseDatos.close()
user = input("Ingrese su apodo: ")
con = input("Ingrese su contraseña: ")
for j in datos["jugadores"]:
    if j["apodo"] == user and j["Contrase\u00f1a"] == con:
        print("Bienvenido/a", j["apodo"])
        menu2()
        option = int(input("Ingrese opción: "))
        if option == 1:
            n = j["nombre"]
            new = input("Cúal será tu nuevo nombre: ")
            modificar("BaseDeDatosJ.json", str(n), str(new))
            print("Has modificado tu nombre")
        elif option == 2:
            n = j["Contrase\u00f1a"]
            new = input("¿Cúal será tu nueva contraseña?: ")
            modificar("BaseDeDatosJ.json", str(n), str(new))
            print("Has modificado tu contraseña")
        elif option == 3:
            n = j["apodo"]
            new = input("¿Cúal será tu nuevo apodo?: ")
            modificar("BaseDeDatosJ.json", str(n), str(new))
            print("Has modificado tu apodo")
        elif option == 4:
            n = j["edad"]
            new = input("¿Cúal es tu edad?: ")
            modificar("BaseDeDatosJ.json", str(n), str(new))
            print("Has modificado tu edad")"""