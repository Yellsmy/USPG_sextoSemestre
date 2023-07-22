import json
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove, system
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
    
#CREACIÓN DE CLASE 
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
                    BarraProgreso(1)
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

    def Modificar_Datos(self,v_user,v_con):
        BaseDatos = open("BaseDeDatosJ.json", "r")
        datos = json.load(BaseDatos)
        BaseDatos.close()
        for j in datos["jugadores"]:
            if j["apodo"] == v_user and j["Contraseña"] == v_con:
                print("Hola", j["apodo"])
                option = menu2()
                if option == 1:
                    n = j["nombre"]
                    new = input("Cúal será tu nuevo nombre: ")
                    modificar("BaseDeDatosJ.json", str(n), str(new))
                    BarraProgreso(0.5)
                    print("Has modificado tu nombre")
                elif option == 2:
                    n = j["Contraseña"]
                    new = input("¿Cúal será tu nueva contraseña?: ")
                    modificar("BaseDeDatosJ.json", str(n), str(new))
                    BarraProgreso(0.5)
                    print("Has modificado tu contraseña")
                elif option == 3:
                    n = j["apodo"]
                    new = input("¿Cúal será tu nuevo apodo?: ")
                    modificar("BaseDeDatosJ.json", str(n), str(new))
                    BarraProgreso(0.5)
                    print("Has modificado tu apodo")
                elif option == 4:
                    n = j["edad"]
                    new = input("¿Cúal es tu edad?: ")
                    modificar("BaseDeDatosJ.json", str(n), str(new))
                    BarraProgreso(0.5)
                    print("Has modificado tu edad")
                else:
                    print("La opción elegida es incorrecta")
                    print("Intente nuevamente")
                    main()
        time.sleep(4)
        os.system ("cls")
        main()

    def Avatar(self,v_user,v_con):
        lista = [["1","Avatar 1","10","10"], ["2","Avatar 2", "10","10"],["3","Avatar 3", "10", "10"]]
        Historial_temp = []
        print("Avatar disponibles")
        with open("BaseDeDatosJ.json") as f:
            data = json.load(f)
        for j in data["jugadores"]:
            if j["apodo"] == v_user and j["Contraseña"] == v_con:
                for i in lista:
                    temp = i[1]
                    print (i[0]+"."+i[1])
                Av = input("Elige tu avatar: ")
                for i in lista:
                    if Av == i[0]:
                        N_Av = i[1]
                        Historial_temp.append((j["apodo"],N_Av))
        os.system ("cls")
        main()
                
#FUNCIONES GENERALES:
# Función para iniciar sesión y retorna las variables
#correspondientes para modificar datos
def Log2():
    BaseDatos = open("BaseDeDatosJ.json", "r")
    datos = json.load(BaseDatos)
    BaseDatos.close()
    user = input("Ingrese su apodo: ")
    con = input("Ingrese su contraseña: ")
    for j in datos["jugadores"]:
        if j["apodo"] == user and j["Contraseña"] == con:
            print("Bienvenido/a", j["apodo"])
            user = j["apodo"]
            con = j["Contraseña"]
            return([user,con])
        if j["apodo"] != user and j["Contraseña"] != con:
            print("Tu usuario y contraseña no coinciden")
            print("Intenta nuevamente")
            main()
    



# Función para modificar los datos                         
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

#Menú para elegir el dato que se desea modificar
def menu2():
    print("¿Qué dato quieres modificar?")
    print("1.Nombre")
    print("2.Contraseña")
    print("3.Apodo")
    print("4. Edad")
    optionTemp = int(input("Ingrese opción: "))
    return optionTemp 

def BarraProgreso(t):
    banner = ["█","10%", "██", "20%", "███","30%","████","40%","█████","50%","██████", "60%","███████",\
    "70%","████████","80%","█████████","90%","█████████","100%"] 
    L = len(banner)
    n = 1
    for j in range(0,n):
        for i in range(0,L):
            os.system("cls")
            print(banner[i])
            time.sleep(1)

#Segundo Menú cuando se inicia sesión
def segundoM():
    print("1. Modificar datos")
    print("2. Elegir avatar")
    Seleccion = int(input("Ingrese opción: "))
    os.system ("cls")
    return Seleccion    

def main():
    op2 = Menú()	
    if op2 == "1":
        #Creacion()
        jugador = Jugadores()
        jugador.registro()	
    elif op2 == "2":
        datos = Log2()
        v_user = datos[0]
        v_con = datos[1]
        print ("Los datos en la lista son ", v_user, v_con )
        sel = segundoM()
        print("Dentro del menú", sel)
        if sel == 1:
            print("aqui",sel)
            jugador = Jugadores()
            jugador.Modificar_Datos(v_user,v_con)
        elif sel == 2:
            jugador = Jugadores()
            jugador.Avatar(v_user,v_con)
main()