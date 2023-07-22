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
        except FileNotFoundError:
            print("Archivo no existe")
        Datos = ""
        lista = []
        
        while True:
            estado = "Activa"
            nombre = input("Ingrese nombre: ")
            nacionalidad = input("Ingrese su nacionalidad: ")
            if nacionalidad.isalpha():
                pass
            else:
                print("Solo letras del alfabeto")
                break
            apodo = input("Ingrese su apodo: ")
            if len(apodo)>8:
                print("Maximo 8 letras")
                break
            try:
                edad = int(input("Ingrese su edad: "))
                if edad > 4:
                    pass
                else: 
                    print("No eres apto")
                    break
            except ValueError:
                print("Solo datos numericos")
            
            contraseña = input("Cree su contraseña: ")      
            repit_contraseña = (input("Confirme su contraseña: "))
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


        a.write(Datos)
        a.close()
        try:
            a = open("Jugadores.txt", "r")
        except FileNotFoundError:
            print("Archivo no existe")

        Lineas = a.readlines()
        for linea in Lineas:
            linea = linea.replace("\n", "").split("|")
            lista.append(linea)
        a.close
		
jugador = Jugadores()
jugador.registro()

