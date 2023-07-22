class persona():
    def __init__(self,nombre,cargo,edad):
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad

    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)

    def caminar(self,pasos):
        self.pasos = pasos
        print("Los pasos dados son: ", pasos)

    def escuchar(self,comprension):
        self.comprension = comprension
        if comprension == "si":
            print("Mensaje comprendido")
        if comprension == "no":
            print("Mensaje no comprendido")

class Rector(persona):
    def __init__(self):
        pass

    def organizar(self, instruccion):
        cargo = self.cargo
        if cargo == "rector":
            self.instruccion = instruccion
            print("Las instrucciones dadas son: ",instruccion)
    
class Decano(persona):
    def __init__(self, escuela):
        self.escuela = escuela

    def escuela_cargo(self):
        print("Administro en la escuela ",self.escuela)

    def hablar(self, mensaje):
        m = self.mensaje
        print("El mensaje del rector de la escuela {} es:".format(m), self.mensaje)


class Catedratico(persona):
    def __init__(self, clases,salario):
        self.clases = clases
        self.salario = salario

    def hablar(self, mensaje):
        print(mensaje)
        confirmacion = input("Has comprendido el mensaje? ")
        if confirmacion == "si":
            print("Felicidades, has comprendido el mensaje")

    def escuchar(self, comprension):
        return super().escuchar(comprension)

def objeto():

    person1 = persona("Lili","catedratico","24")
    person1.caminar("9000")
    person1 = Catedratico("Programación","4,000")
    person1.hablar("El día de hpy no habra clases")

    person2 = persona("Harold","rector","55")
    person2 = Rector()
    person2.organizar("El 1 de noviembre no se trabaja")


objeto()