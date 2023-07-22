
class Persona:
    def __init__(self,nombre,dpi):
        self.nombre = nombre
        self.dpi = dpi

    def hablar(self, *palabras):
        for frase in palabras:
            print (self.nombre, ":", frase) 

luis = Persona("Luis","2456890761415")
luis.hablar("Hola", "soy Luis", "Mucho gusto")

class Cuentahabiente(Persona):
    def __init__(self, cuenta, saldo):
        self.cuenta = cuenta
        self.__saldo = saldo

    #Esta es una funsion
    #Para hacer privada alguna información se debe agregar __ al nombre
    #de la opcion que quiero hacer privada
    def consultarSaldo(self):
        return self.__saldo

Cuentahabiente1 = Cuentahabiente("1111111110",250)
Cuentahabiente1.nombre = "Mario"
Cuentahabiente1.dpi = "12334568790"
saldo = Cuentahabiente1.consultarSaldo()
print (Cuentahabiente1.nombre,"Tu saldo es " ,saldo)
#Si muestra el saldo porque se está ejecutando la funcion y no la variable
print("Su saldo es ", Cuentahabiente1.consultarSaldo())
#Se está ejecutando la variable. Muestra error porque está privado
print("Su saldo es: ", Cuentahabiente1.__saldo)


#CADENAS
#Se puede hacer uso de métodos y definidos con cadena de caracteres

cadena = "Este es el valor de la cadena de caracteres"

#Upper es para pasarlo todo a mayúscula
print(cadena.upper())
#dir muestra todas las funciones de string que tiene cadena
print(dir(cadena))

print("____________")
cadena2 = 123
#dir muestra todas las funciones de número que tiene cadena
print(dir(cadena2))



#Se debe aplicar el encapsulamiento, por ejemplo
#Incorrecto, pedir que se ejecute directamente una variable
print("Su saldo es: ", Cuentahabiente1.saldo)

#Correcto, crear metodos y funciones para que nos muestren valores
    def darSaldo():
        return self.saldo
print("Su saldo es: ", cuentahabiente1.darSaldo())

