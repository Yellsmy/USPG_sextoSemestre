import json
from tempfile import mkstemp
from os import fdopen, remove, system
from shutil import move
class tarjeta():
    def __init__(self,nombre, numero, tipo, total, gasto):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.total = total
        self. gasto = gasto
    def consultar(self):
        print("Susaldo es "+self.total)

class Premiun(tarjeta):
    def operacion(self):
        calculo = 10 * int(self.gasto) / 100
        newD= int(self.total)+ int(calculo)
        modificar("DataBase.json",str(self.total),str(newD))
        self.total = str(newD)
        print("Acumulación exitosa")
    def consultar(self):
        print ("Usted tiene "+ self.total + " de dinero acumulado")


class Platino(tarjeta):
    def calculo(self):
        if self.gasto >= 500:
            cont = self.gasto/500
            calculo = 500*int(cont)
            newD= int(self.total)+ int(calculo)
            modificar("DataBase.json",str(self.total),str(newD))
            self.total = str(newD)
            print("Acumulación exitosa")
    def consultar(self):
        print("Sus puntos acumulados son "+ self.total)

def modificar(archivo, antiguo_dato, nuevo_dato):
    Antiguo, Nuevo = mkstemp()
    with fdopen(Antiguo,'w') as nueva_fila:
        with open(archivo) as vieja_linea:
            for linea in vieja_linea:
                nueva_fila.write(linea.replace(antiguo_dato, nuevo_dato))
    remove(archivo)
    move(Nuevo, archivo)

def Menú():
    print(" ________________________")
    print("|       BIENVENIDO       |")
    print("|________________________|")
    print("Presiona 1 para iniciar")
    op = int(input("> "))
    return op  

def main():
    while True:
        seleccion = Menú()
        if seleccion == 1:
            with open("DataBase.json") as f:
                datos = json.load(f)
            n_tarjeta = input("Ingrese número de tarjeta: ")
            for j in datos["clientes"]:
                if n_tarjeta == j["cuenta"]:
                    numero = j["cuenta"]
                    nombre = j["nombre"]
                    tipo = j["tarjeta"]
                    total = j["acumulacion"]
                    print("Bienvenido/a"+ j["nombre"])
                    gasto = int(input("Ingrese el monto gastado: "))
                    gast = gasto
                    if tipo == "Premium":
                        Cliente = Premiun(nombre,numero,tipo,total,gast)
                        Cliente.operacion()
                    elif tipo == "Platino":
                        Cliente = Platino(nombre,numero,tipo,total,gast)
                        Cliente.calculo()
                    print("¿Desea consultar su saldo?")
                    print("1.Sí")
                    print("2.Salir")
                    opcion = int(input("Ingrese opción: "))
                    n_tarjeta = input("Ingrese número de tarjeta: ")
                    if n_tarjeta == j["cuenta"]:
                        if opcion == 1:
                            if tipo == "Premium":
                                Cliente = Premiun(nombre,numero,tipo,total,gast)
                                Cliente.consultar()
                            elif tipo == "Platino":
                                Cliente = Platino(nombre,numero,tipo,total,gast)
                                Cliente.consultar()
                        if opcion == 2:
                            print("Gracias por utilizar nuestro servicio")
                            break
            print("Numero no encontrado")
main()