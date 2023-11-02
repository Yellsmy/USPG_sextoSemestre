"""class Mayor():
    elif edad >= int(j["EdadInicio"]) and edad <= int(j["EdadFinal"]):
            fase = "2"
            print("fase 2")
            print("repit")
            print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= int(j["EdadInicio"]) and edad <= int(j["EdadFinal"]):
            fase = "3"
            print("fase 3")
            print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= int(j["EdadInicio"]) and edad <= int(j["EdadFinal"]):
            fase = "4"
            print("fase 4")
            print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= int(j["EdadInicio"]) and edad <= int(j["EdadFinal"]):
            fase = "5"
            print("fase 5")
            print(j["EdadInicio"],j["EdadFinal"])
            with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json","r") as f:
    dato = json.load(f)
for i in dato["Grupos"]:
            print(i["EdadInicio"])

def AsignacionFase(edad):
    fase=""
    with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json","r") as f:
            dato = json.load(f)
    for j in range(0,5):
        #print("edad", self.edad)
        #print(j["EdadInicio"])
        if edad >= 60 and edad <= 150:
            fase = "1"
            print("fase 1")
            #print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= 40 and edad <= 59:
            fase = "2"
            print("fase 2")
            print("repit")
            #print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= 19 and edad <= 39:
            fase = "3"
            print("fase 3")
            #print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= 12 and edad <= 18:
            fase = "4"
            print("fase 4")
            #print(j["EdadInicio"],j["EdadFinal"])
        elif edad >= 5 and edad <= 11:
            fase = "5"
            print("fase 5")
            #print(j["EdadInicio"],j["EdadFinal"])
    return fase

        
        self.nombres = ""
        self.apellidos=""
        self.fNacimiento = ""
        self.sexo = ""
        self.email = ""
        self.telefono =""
        self.eCongenita = ""
        self.eAutoinmune = ""
        self.edad = ""
        self.dosis =""
        self.fase = """
import json

def Archivo():
    data = {}
    data["Personas"] = []
    data ["Personas"].append({
            "nombres" :"nombres",
            "apellidos" :"apellidos", 
            "edad" :"edad",
            "email" :"email",
            "telefono" :"telefono",
            "sexo" :"sexo",
            "eCongenita" :"eCongenita",
            "eAutoinmune" : "eAutoinmune",
            "fNacimiento" : "fNacimiento",
            "dosis" :"dosis",
            "Fase": "fase",
            "cita": "cita"})
    with open("RegistroPersonas.json", "w") as file:
        json.dump(data, file, indent=5, ensure_ascii=False)

Archivo()

def Archivo2():
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
    with open("Prueba.json", "w") as file:
        json.dump(data, file, indent=5, ensure_ascii=False)

Archivo2()


"""FechaActual = datetime.datetime.now().strftime("%d/%m/%Y")
print(FechaActual)
with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json") as file:
    dato = json.load(file)
fechaC = fecha()
for j in dato["Grupos"]:
    FechaInicio = j["FechaInicio"]
    FechaInicio = datetime.datetime.strptime(FechaInicio, "%d/%m/%Y")
    FechaActual = datetime.now()
    if FechaInicio > FechaActual:
        print("Lo sentimos, la fecha no es aceptable")
#dia = fechaA.day
#mes = fechaA.month
#anio = fechaA.year
#fInicio = date(anio,mes,dia)
#fFinal = date(2022,11,30)"""

"""a = open("InfoCitas.txt","w")
a.write("0|0")
a.close()
print("Archivo creado")

lis =[]
def prueba(fInicio,fFinal):
    for i in range(int((fFinal - fInicio).days)):
        lis.append(fInicio + timedelta(i))
    print("La funcion de generacion de fechas esta lista")
    #print(fechas)
#print()
prueba(fInicio,fFinal)
fechas =[]
for dato in lis:
    fechas.append(dato)
    print(dato[3])
print(fechas)


def AbrirArchivotxt():
    a = open("InfoCitas.txt", "r")
    lineas= a.readlines()
    ListaDatos = []
    for linea in lineas:
        linea = linea.replace("\n", "").split("|")
        ListaDatos.append(linea)
    a.close()
    print("La funcion de Abrir Archivo esta lista")
    return ListaDatos


def GenerarCita(lista):
    lista = AbrirArchivotxt()
    NewCita = ""
    while True:
        for i in lista:
            NumCitas = int(i[0])
            PosicionF = int(i[1])
            if NumCitas <= 100:
                for j in lista:
                    NewCita = j[PosicionF]
                NumCitas =+ 1
                datos = str(NumCitas)+"|"+str(PosicionF)
                a = open("BaseDeDatos.txt","w")
                a.write(datos)
                a.close()
                break
            elif NumCitas > 100:
                PosicionF =+ 1
                datos = "0"+"|"+str(PosicionF)
                a = open("BaseDeDatos.txt","w")
                a.write(datos)
                a.close()
                break
        print("Su nueva cita es", NewCita)
        print("La Generacion de cita esta lista")
        return NewCita



#GenerarCita(fechas)  """
        

	
        

"""a = datetime.datetime.today()
numdays = 100
dateList = []
for x in range (0, numdays):
    dateList.append(fInicio - datetime.timedelta(days = x))
print(dateList)
for dato in dateList:
    print(dato.strftime("%Y-%m-%d"))
    

def generar(fInicio, fFinal):
    fechas = []
    dias = (fFinal-fInicio).days
    for i in range(dias):
        fechas.append(fInicio+timedelta(i))
        return fechas

resultado = generar(fInicio,fFinal) 

for f in resultado:
    print(f)"""
    
"""def prueba(fInicio,fFinal):
    for i in range(int((fFinal - fInicio).days)):
        yield fInicio + timedelta(i)
        
for dato in prueba(fInicio,fFinal):
    print(dato.strftime("%Y-%m-%d"))


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))

dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

fechaNacimiento = date(anio,mes,dia)

calculo = fechaA.year - fechaNacimiento.year
calculo -= ((fechaA.month, fechaA.day) < (fechaNacimiento.month, fechaNacimiento.day))

print("Tu edad es: ", calculo)"""

"""class Prueba():
    def __init__(self):
        self.__variable= 2

    def operacion(self):
        #print("adentro")
        while self.__variable > 1:
            print("Logrado")

objeto = Prueba()
objeto.operacion()
import json
#import datetime
from datetime import date
from pruebas0 import fecha, ValidacionFecha, GrabarDatos, AsignacionFase
#from datetime import date
#from random import randint

class Persona():
    def __init__(self):
        #fechaA = datetime.datetime.now()
        #dia = fechaA.day
        #mes = fechaA.month
        #anio = fechaA.year
        self.fechaAct= date.today()
        self.nombres = ""
        self.apellidos=""
        self.fNacimiento = ""
        self.sexo = ""
        self.email = ""
        self.telefono =""
        self.eCongenita = ""
        self.eAutoinmune = ""
        self.edad = 0
        self.fase = ""

    def registro(self):
        self.nombres = input("Nombres: ")
        self.apellidos = input("Apellidos: ")
        print("Fecha de Nacimiento: (en números)")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        self.fNacimiento = date(anio,mes,dia)
        self.sexo= input("Sexo: ")
        self.email = input("Correo Electrónico: ")
        self.telefono = input("No. Telefóno/Celular: ")
        val = input("¿Padeces de alguna enfermedad Congénita?: ").upper()
        if val == "SI" or val =="SÍ":
            self.eCongenita = True
        elif val == "NO":
            self.eCongenita = False
        else:
            self.eCongenita = "No especificado"
        val2 = input("¿Padeces de alguna enfermedad autoinmune?: ").upper()
        if val2 == "SI" or val =="SÍ":
            self.eAutoinmune = True
        elif val2 == "NO":
            self.eAutoinmune = False
        else:
            self.eAutoinmune = "No especificado"
        self.dosis = input("Dosis: ")
        calculo = self.fechaAct.year - self.fNacimiento.year
        calculo -= ((self.fechaAct.month, self.fechaAct.day) < (self.fNacimiento.month, self.fNacimiento.day))
        self.edad = calculo
        print("calculo", calculo)
        with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json","r") as f:
            dato = json.load(f)
        print(dato)

class Fase1(Persona):
    def __init__(self):
        Persona().__init__()
        self.fase = AsignacionFase(int(self.edad))
    def GenerarCita(self):
        acceso = ValidacionFecha(self.fase)
        if acceso == True: #>= self.edad and j["EdadFinal"]  <= self.edad:
            self.cita = fecha()
            GrabarDatos(self.nombres,self.apellidos,str(self.edad),self.email,self.telefono,self.sexo,self.eCongenita,self.eAutoinmune,self.fNacimiento,self.dosis,self.fase,self.cita)
            print("Su cita es la fecha ", self.cita)
            print("Por favor llevar su documento de identificación")
        elif acceso == False:
            print("su fase no comienza")

class Fase2(Persona):
    pass
    #def Cita(self):

class Fase3(Persona):
    pass
    #def Cita(self):

class Fase4(Persona):
    pass
    #def Cita(self):

class Fase5(Persona):
    pass
    #def Cita(self):    



#Nombres,teléfono, padece enfermedad congénita(S,N), padece enfermedad autoinmune(S,N), Dosis(1,2)
objeto = Persona()
objeto.registro()
objeto2 = Fase1()
objeto2.GenerarCita()"""