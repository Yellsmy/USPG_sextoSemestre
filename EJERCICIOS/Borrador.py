import json
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import os
import time
def Archivo():
    data = {}
    data["jugadores"] = []
    data ["jugadores"].append({
                "nombre" :"Prueba",
                "Contraseña": "123", 
                "nacionalidad" :"Guatemalteca",
                "apodo" : "Prueba1",
                "edad" : "24",
                "estado" : "Inactiva",
                "Total_Puntos":"0"})
    data["Historial"] = []
    data["Historial"].append({
    "Apodo":"Lily",
    "Avatar_Usado" : "AvatarPrueba"})
    with open("BaseDeDatosJ.json", "w") as file:
        json.dump(data, file, indent=5, ensure_ascii=False)




def Menú():
    print(" ________________________")
    print("|       BIENVENIDO       |")
    print("|________________________|")
    print("1. Registrarme")
    print("2. Iniciar sesión")
    op = input("Ingrese opción: ")
    os.system ("cls")
    return op
    

class Jugadores():
    def __init__(self):
        nombre = " "
        nacionalidad = ""
        apodo = ""
        edad = 0
        puntos_Totales = 0
        contraseña = ""
        estado = ""
        
    def cargarUsuario(self,nombre, contraseña, nacionalidad, edad, apodo, estado,puntos_Totales):
        try:
            self.nombre = nombre
            self.contraseña = contraseña
            self.nacionalidad = nacionalidad
            self.apodo = apodo
            self.edad = edad
            self.estado = estado
            self.puntos_Totales = puntos_Totales
        except TabError:
            print("Error de tabulación")
            os.system ("cls")

    def registro(self):
            BaseDatos = open("BaseDeDatosJ.json", "r")
            dat = json.load(BaseDatos)
            BaseDatos.close()
            for j in dat["jugadores"]:
                Ap = j["apodo"]
                print(Ap)
            while True:
                try:
                    estado = "Activa"
                    puntos_Totales = 0
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
                                print("Dentro del segundo de la validación")
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
                    "estado" : estado,
                    "Puntos Totales": puntos_Totales}
                    with open("BaseDeDatosJ.json") as file:
                        datos = json.load(file)
                        datos["jugadores"].append(x)
                    with open("BaseDeDatosJ.json", "w") as file:
                        json.dump(datos, file, indent=6, ensure_ascii=False)
                    os.system("cls")
                    print("Estamos creando tu cuenta")
                    time.sleep(10)
                    print(" ________________________")
                    print("|     ¡¡FELICIDADES!!    |")
                    print("|  HAS CREADO TU CUENTA  |")
                    print("|________________________|")
                    self.cargarUsuario(nombre, nacionalidad, contraseña, apodo, edad,estado,puntos_Totales)
                    break
                except ValueError:
                    print("Error, su edad debe ser en números y no en letras, inténtelo nuevamente")
            main()
            os.system ("cls")

    def Modificar_Datos(self):
        #with open("BaseDeDatosJ.json") as f:
           # data = json.load(f)
        BaseDatos = open("BaseDeDatosJ.json", "r")
        datos = json.load(BaseDatos)
        BaseDatos.close()
        print(datos)
        usuarios= datos["jugadores"]
        for j in usuarios:
            apodos = j["apodo"]
            print(apodos)
        option = menu2()
        if option == 1:
            n = j["nombre"]
            new = input("Cúal será tu nuevo nombre: ")
            modificar("BaseDeDatosJ.json", str(n), str(new))
            print("Has modificado tu nombre")
        elif option == 2:
            n = j["Contraseña"]
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
            print("Has modificado tu edad")
        else:
            print("La opción elegida es incorrecta")
            print("Intente nuevamente")
            main()
        os.system ("cls")

    def Avatar(self):
        lista = [["1","Avatar 1","10","10"], ["2","Avatar 2", "10","10"],["3","Avatar 3", "10", "10"]]
        print("Avatar disponibles")
       
        for i in lista:
            temp = i[1]
            print (i[0]+"."+i[1])
        Av = input("Elige tu avatar: ")
        for i in lista:
            if Av == i[0]:
                N_Av = i[1]
                #print(N_Av)
        Historial_temp = []

    def Login(self):
        with open("BaseDeDatosJ.json") as f:
            data = json.load(f)
            
        BaseDatos = open("BaseDeDatosJ.json", "r")
        datos = json.load(BaseDatos)
        BaseDatos.close()
        user = input("Ingrese su apodo: ")
        con = input("Ingrese su contraseña: ")
        for j in datos["jugadores"]:
            if j["apodo"] == user and j["Contraseña"] == con:
                print("Bienvenido/a", j["apodo"])
                print(j["apodo"], j["Contraseña"],j["edad"])
                        




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
    optionTemp = int(input("Ingrese opción: "))
    return optionTemp


        
    while True:
        print(valA,valC)
        if user != valA and con != valC:
            print(valA,valC)
            print("Lo sentimos, tu usuario no aparece en los datos")
            print("Intente nuevamente")
            user = input("Ingrese su apodo: ")
            con = input("Ingrese su contraseña: ")
        elif user == valA and con == valC:
            print(valA,valC)
            print("Bienvenido/a", valA)
            break
        
            

def New_menu():
    print("1. Modificar datos")
    print("2. Elegir Avatar")
    print("¿Qué deseas hacer?")
    Selec= int(input(": "))
    return Selec
                    


def Creacion():
    jugador = Jugadores()
    jugador.registro()

def Mod():
    jugador = Jugadores()
    jugador.Modificar_Datos()
def Selc_Avatar():
    jugador = Jugadores()
    jugador.Avatar()

def ingreso():
    jugador = Jugadores()
    jugador.Login()

def main():
    op2 = Menú()	
    if op2 == "1":
        Creacion()	
    elif op2 == "2":
        ingreso()
        Sel = New_menu()
        if Sel == 1:
            print("Hasta aquí")
            Mod()
        elif Sel == 2:
            Selc_Avatar()  

main()




import json
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import os
import time
def Archivo():
    data = {}
    data["jugadores"] = []
    data ["jugadores"].append({
                "nombre" :"Prueba",
                "Contraseña": "123", 
                "nacionalidad" :"Guatemalteca",
                "apodo" : "Prueba1",
                "edad" : "24",
                "estado" : "Inactiva",
                "Total_Puntos":"0"})
    data["Historial"] = []
    data["Historial"].append({
    "Apodo":"Lily",
    "Avatar_Usado" : "AvatarPrueba"})
    with open("BaseDeDatosJ.json", "w") as file:
        json.dump(data, file, indent=5, ensure_ascii=False)




def Menú():
    print(" ________________________")
    print("|       BIENVENIDO       |")
    print("|________________________|")
    print("1. Registrarme")
    print("2. Modificar datos")
    print("3. Elegir avatar")
    op = input("Ingrese opción: ")
    os.system ("cls")
    return op
    

class Jugadores():
    def __init__(self):
        nombre = " "
        nacionalidad = ""
        apodo = ""
        edad = 0
        puntos_Totales = 0
        contraseña = ""
        estado = ""
        
    def cargarUsuario(self,nombre, contraseña, nacionalidad, edad, apodo, estado,puntos_Totales):
        try:
            self.nombre = nombre
            self.contraseña = contraseña
            self.nacionalidad = nacionalidad
            self.apodo = apodo
            self.edad = edad
            self.estado = estado
            self.puntos_Totales = puntos_Totales
        except TabError:
            print("Error de tabulación")
            os.system ("cls")

    def registro(self):
            BaseDatos = open("BaseDeDatosJ.json", "r")
            dat = json.load(BaseDatos)
            BaseDatos.close()
            for j in dat["jugadores"]:
                Ap = j["apodo"]
                print(Ap)
            while True:
                try:
                    estado = "Activa"
                    puntos_Totales = 0
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
                                print("Dentro del segundo de la validación")
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
                    "estado" : estado,
                    "Puntos Totales": puntos_Totales}
                    with open("BaseDeDatosJ.json") as file:
                        datos = json.load(file)
                        datos["jugadores"].append(x)
                    with open("BaseDeDatosJ.json", "w") as file:
                        json.dump(datos, file, indent=6, ensure_ascii=False)
                    os.system("cls")
                    print("Estamos creando tu cuenta")
                    time.sleep(10)
                    print(" ________________________")
                    print("|     ¡¡FELICIDADES!!    |")
                    print("|  HAS CREADO TU CUENTA  |")
                    print("|________________________|")
                    self.cargarUsuario(nombre, nacionalidad, contraseña, apodo, edad,estado,puntos_Totales)
                    break
                except ValueError:
                    print("Error, su edad debe ser en números y no en letras, inténtelo nuevamente")
            main()
            os.system ("cls")

    def Modificar_Datos(self):
        #with open("BaseDeDatosJ.json") as f:
           # data = json.load(f)
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
                option = menu2()
                if option == 1:
                    n = j["nombre"]
                    new = input("Cúal será tu nuevo nombre: ")
                    modificar("BaseDeDatosJ.json", str(n), str(new))
                    print("Has modificado tu nombre")
                elif option == 2:
                    n = j["Contraseña"]
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
                    print("Has modificado tu edad")
                else:
                    print("La opción elegida es incorrecta")
                    print("Intente nuevamente")
                    main()
        os.system ("cls")
        main()

    def Avatar(self):
        lista = [["1","Avatar 1","10","10"], ["2","Avatar 2", "10","10"],["3","Avatar 3", "10", "10"]]
        Historial_temp = []
        print("Avatar disponibles")
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
                for i in lista:
                    temp = i[1]
                    print (i[0]+"."+i[1])
                Av = input("Elige tu avatar: ")
                for i in lista:
                    if Av == i[0]:
                        N_Av = i[1]
                        Historial_temp.append((j["apodo"],N_Av))
                        print(Historial_temp)
                
                        
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
    optionTemp = int(input("Ingrese opción: "))
    return optionTemp 

def Avatar():
        lista = [["1","Avatar 1","10","10"], ["2","Avatar 2", "10","10"],["3","Avatar 3", "10", "10"]]
        Historial_temp = []
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
                print("Avatar disponibles")
                for i in lista:
                    temp = i[1]
                    print (i[0]+"."+i[1])
                Av = input("Elige tu avatar: ")
                for i in lista:
                    if Av == i[0]:
                        N_Av = i[1]
                        Historial_temp.append([j["apodo"],N_Av])
                        print(Historial_temp)

def Creacion():
    jugador = Jugadores()
    jugador.registro()
def Mod():
    jugador = Jugadores()
    jugador.Modificar_Datos()
#def Selc_Avatar():
    #jugador = Jugadores()
    #jugador.Avatar()


def main():
    op2 = Menú()	
    if op2 == "1":
        Creacion()	
    elif op2 == "2":
        Mod()
    elif op2 == "3":
        Avatar()
  

main()