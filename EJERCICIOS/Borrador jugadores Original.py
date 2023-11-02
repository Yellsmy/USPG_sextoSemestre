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


