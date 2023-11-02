from datetime import date
from pruebas0 import fecha, ValidacionFecha, GrabarDatos, AsignacionFase


class Persona: #SÚPER CLASE
    def __init__(self):
        while True:
            try:
                self.fechaAct= date.today()
                self.nombres = input("Nombres: ")
                self.apellidos = input("Apellidos: ")
                print("Fecha de Nacimiento: (en números)")
                dia = int(input("Día: "))
                mes = int(input("Mes: "))
                anio = int(input("Año: "))
                self.fNacimiento = date(anio,mes,dia)
                self.sexo= input("Sexo: ")
                self.email = input("Correo Electrónico: prueba@example.com ")
                self.telefono = int(input("No. Telefóno/Celular (Solo números): "))
                val = input("¿Padeces de alguna enfermedad Congénita? (SI/NO): ").upper()
                if val == "SI" or val =="SÍ":
                    self.eCongenita = "Sí"
                elif val == "NO":
                    self.eCongenita = "No"
                else:
                    self.eCongenita = "No especificado"
                val2 = input("¿Padeces de alguna enfermedad autoinmune? (SI/NO): ").upper()
                if val2 == "SI" or val =="SÍ":
                    self.eAutoinmune = "Sí"
                elif val2 == "NO":
                    self.eAutoinmune = "No"
                else:
                    self.eAutoinmune = "No especificado"
                self.dosis = int(input("Dosis (1/2): "))
                calculo = self.fechaAct.year - self.fNacimiento.year
                calculo -= ((self.fechaAct.month, self.fechaAct.day) < (self.fNacimiento.month, self.fNacimiento.day))
                self.edad = calculo
                self.fase = AsignacionFase(self.edad)
                break
            except ValueError:
                    print("Error, recuerde que su edad, teléfono y dosis deben ser específicadas con números")

    def MostrarCita(self):
        print("Gracias por utilizar nuestra plataforma")
        print("Por favor no olvide llevar su Documento de Identificación")
        print("  GOBIERNO DE GUATEMALA  ")
        print("Juntos saldrémos adelante")


class Fases(Persona): #CLASE HIJA
    def GenerarCita(self):
        acceso = ValidacionFecha(self.fase)
        if acceso == "si":
            self.cita = fecha()
            GrabarDatos(self.nombres,self.apellidos,str(self.edad),self.email,str(self.telefono),self.sexo,str(self.eCongenita),str(self.eAutoinmune),str(self.fNacimiento),str(self.dosis),self.fase,str(self.cita))
        elif acceso == "no":
            print("Lo sentimos, su fase de vacunación no ha llegado")
            print("Verifique las fechas de inicio y todas las fases","\n","En nuestras plataformas e intente nuevamente")
        return acceso

    def MostrarCita(self):
        print("Gracias por utilizar nuestra plataforma")
        print("Usted pertenece a la fase {}".format(self.fase))
        print("Su cita es el {}. Por favor no olvide llevar su Documento de Identificación".format(self.cita))
        print("O partida de nacimiento si es menor de edad")
        print("_________________________")
        print("  GOBIERNO DE GUATEMALA  ")
        print("Juntos saldrémos adelante")

def Inicio(): #FUNCIÓN PARA EVALUAR SI LA PERSONA SE PUEDE REGISTRAR O NO
    objeto2 = Fases()
    acceso = objeto2.GenerarCita()
    if acceso == "si":
        objeto2.MostrarCita()
    elif acceso == "no":
        print("_________________________")
        print("  GOBIERNO DE GUATEMALA  ")
        print("Juntos saldrémos adelante")

Inicio()