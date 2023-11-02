class figura():
    def __init__(self):
        self.nfigura = ""

class rectangulo(figura):
    def __init__(self):
        figura().__init__()
        self.largo =float(input("Ingrese largo: "))
        self.ancho = float(input("Ingrese ancho: "))
    def calculo(self):
        self.area = self.largo * self.ancho
        print("El área de su rectángulo es {}".format(self.area)) 

class cuadrado(figura):
    def __init__(self):
        super().__init__()
        self.lado = float(input("Ingrese lado: "))
    def calculo(self):
        self.area = self.lado**2
        print("El área de su cuadrado es {}".format(self.area)) 

class triangulo(figura):
    def __init__(self):
        figura().__init__()
        self.base = float(input("Ingrese base: "))
        self.altura = float(input("Ingrese altura: "))
    def calculo(self):
        self.area = self.base * self.altura /2
        return print("El área de su triángulo es",self.area)

class circulo(figura):
    def __init__(self):
        figura().__init__()
        self.radio = float(input("Ingrese radio: "))
    def calculo(self):
        self.area = 3.1416 * self.radio **2
        print("El área de su círculo es {}".format(self.area)) 

def menu():
    print(" >Rectangulo","\n",">Cuadrado","\n",">Triangulo","\n",">Circulo","\n",">Presiona '5' para Salir")
    while True:
        print("Ingrese la figura para calcular el área")
        forma = figura()
        forma.nfigura = input("> ").upper()
        if forma.nfigura == "RECTANGULO":
            Area = rectangulo()
            Area.calculo()
        elif forma.nfigura == "CUADRADO":
            Area = cuadrado()
            Area.calculo()
        elif forma.nfigura == "TRIANGULO":
            Area = triangulo()
            Area.calculo()
        elif forma.nfigura == "CIRCULO":
            Area = circulo()
            Area.calculo()
        elif forma.nfigura == "5":
            print("¡GRACIAS POR USAR NUESTRO SERVICIO!")
            break
        else:
            print("Tu opción no coincide, intenta nuevamente")
menu()