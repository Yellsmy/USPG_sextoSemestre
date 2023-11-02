#El nombre siempre en singular, la primera letra de cada palabra en mayuscula y lo demás minuscula
class Usuario:
    #Este es el método constructor y el Inicio de los atributos
    def __init__(self,nombre,pin,cuenta, saldo):
        self.nombre = nombre
        self.pin = pin
        self.cuenta = cuenta
        self.saldo = saldo
        self.activo = True
    #Estos son más métodos
    def desactivar(self):
        self.activo = False
    
    def debitar(self,cantidad):
        #Para condicionar solo si esta activo se haga el debito
        #podemos usar un if
        if self.activo:
            self.saldo = self.saldo - cantidad

    def acreditar(self, cantidad):
        if self.activo:
            self.saldo = self.saldo + cantidad

#Este es un objeto, en el que se pone como parametro
#el nombre, pin, cuenta, saldo
usuario1 = Usuario("Mynor","1234","002568745", 10000)

print(usuario1.activo)
print("Bienvenido", usuario1.nombre)
print("Su saldo es", usuario1.saldo)

#Para debitar saldo
usuario1.debitar(5000)
print("Su saldo es", usuario1.saldo)

#para desactivar la cuenta
usuario1.desactivar()
print(usuario1.activo)


class Estudiante:
    def __init__(self, nombre, apellido, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.aprobado = "Aprobado"

    def promedio(self,n1,n2,n3,n4):
        promedio = n1 + n2 + n3 + n4
        self.promedio = promedio/4

    def reprobado(self):
        if self.promedio < 60:
            self.aprobado = "Reprobado"
        else:
            self.aprobado = "Aprobado"

Estudiante1 = Estudiante("Carla", "Pérez", "21")
print("Bienvenido/a", Estudiante1.nombre, Estudiante1.apellido)
Estudiante1.promedio(60,70,80,90) 
print("Su promedio es", Estudiante1.promedio)
Estudiante1.reprobado()
print("Eres un estudiante", Estudiante1.aprobado)


    