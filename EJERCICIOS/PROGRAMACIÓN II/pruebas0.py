from random import randint
import json
from datetime import datetime, date

def ValidacionFecha(Fase): #FUNCIÓN PARA VALIDAR SI LA FECHA DE INICIO DE LA FASE ES MENOR QUE LA FECHA ACTUAL
    acceso = "no"
    fActual= datetime.now().date()
    with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json") as file:
        dato = json.load(file)
    for j in dato["Grupos"]:
        if j["Fase"] == Fase:
            FechaInicio = j["FechaInicio"]
            fInicio = datetime.strptime(FechaInicio, "%Y-%m-%d").date()
            if str(fActual) > str(fInicio):
                acceso = "si"
    return acceso

def fechaAleatoria(): #FUNCIÓN QUE CREA FECHAS ALEATORIAS DE LA FECHA ACTUAL AL 30/6/2022
    fechaA = date.today().toordinal()
    fechaF = date.today().replace(year=2022,month=11,day=30).toordinal()
    fecha = date.fromordinal(randint(fechaA,fechaF))
    return fecha

def fecha(): #FUNCIÓN QUE RETORNA SOLO 1 FECHA ALEATORIA PARA LA CITA 
    f = ""
    for _ in range(1):
        f = fechaAleatoria()
    return f


def GrabarDatos(nombres,apellidos,edad,email,telefono,sexo,eCongenita,eAutoinmune,fNacimiento,dosis,fase,cita): #FUNCIÓN PARA GRABAR LOS DATOS INGRESADOS EN EL ARCHIVO JSON
        x = {
            "nombres" :nombres,
            "apellidos" :apellidos, 
            "edad" :edad,
            "email" :email,
            "telefono" :telefono,
            "sexo" :sexo,
            "eCongenita" :eCongenita,
            "eAutoinmune" : eAutoinmune,
            "fNacimiento" : fNacimiento,
            "dosis" :dosis,
            "Fase": fase,
            "cita": cita}
        with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/RegistroPersonas.json") as file:
            datos = json.load(file)
            datos["Personas"].append(x)
        with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/RegistroPersonas.json", "w") as file:
                json.dump(datos, file, indent=5, ensure_ascii=False)
        print("")
        print("     ¡¡FELICIDADES!!    ")
        print("    TE HAS REGISTRADO   ")
        print("")


def AsignacionFase(edad): #FUNCIÓN QUE EVALUA LA FECHA DE NACIMIENTO CON LA EDAD DE INICIO Y FIN DE CADA FASE Y ASIGNA LA FASE CORRESPONDIENTE
    fase=""
    with open("c:/Users/Lenovo5/Desktop/UNIVERSIDAD SAN PABLO DE GUATEMALA/PROGRAMACION/PROGRAMACIÓN II/GrupoEtario.json","r") as f:
            dato = json.load(f)
    for j in dato["Grupos"]:
        if edad >= int(j["EdadInicio"]) and edad <= int(j["EdadFinal"]):
            fase = j["Fase"]
    return fase
