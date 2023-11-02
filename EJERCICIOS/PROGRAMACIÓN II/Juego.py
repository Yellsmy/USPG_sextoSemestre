
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
            print("Erro de tabulación")

    def registro(self):
        try: 
            a = open("Jugadores.txt", "a+")
            Datos = ""
            lista = []
            
            while True:
                try:
                    estado = "Activa"
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese su edad: "))
                    if edad <= 6:
                        print("Lo sentimos, debes ser mayor de 6 años para registrarte")
                        #edad = int(input("Ingrese su edad: ")) Si queremos que el usuario ingrese
                        #su edad de nuevo y quitamos el break
                        break
                    #Podemos llamar al menú principal
                    nacionalidad = input("Ingrese su nacionalidad: ")
                    apodo = input("Ingrese su apodo: ")
                    with open("Jugadores.txt", "r") as a:
                        for l in a.readlines():
                            if l[1] == apodo:
                                print("Lo sentimos, el apodo", apodo, "ya está en uso")
                                print("Intente nuevamente")
                                apodo = input("Ingrese su apodo: ")
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
                    Datos += nombre + "|"
                    Datos += apodo + "|"
                    Datos += nacionalidad + "|"
                    Datos += str(edad) + "|"
                    Datos += contraseña + "|"
                    Datos += estado + "\n"
                    self.cargarUsuario(nombre, nacionalidad, contraseña, apodo, edad,estado)
                    break
                except ValueError:
                    print("Error, su edad debe ser en números y no en letras, inténtelo nuevamente")


            a.write(Datos)
            a.close()
            a = open("Jugadores.txt", "r")
            Lineas = a.readlines()
            for linea in Lineas:
                linea = linea.replace("\n", "").split("|")
                lista.append(linea)
            a.close
        except FileNotFoundError:
            print("Archivo no existe")
		
jugador = Jugadores()
jugador.registro()



