
class Auto:
    marca= ""
    modelo =0
    placa =""
#Crear el objeto taxi que pertenece a la clase Auto
taxi = Auto()

#Para imprimir debemos usar el print, llamar al objeto
#que será taxi, seguido de un punto que nos podra acceder
#a uno de los atributos
print(taxi.modelo)


class persona:
    doctor = ""

persona.doctor


class jugadores:
    j1 ="Messi"
    j2 ="Cristiano Ronaldo"

print(jugadores.j1)


#primero podemos crear la clase sin ningun atributo
class nombre:
    #Para pasar sin incluir ningún atributo usamos el "pass"
    pass

#Ahora podemos crear las variables para que se incluyan en la clase
victor = nombre() #entre parentesis dejamos prametros vacios si no tenemos datos que incluir
maria = nombre()

#Para crear un atributo para cada uno usamos la regla
#objeto.atributo = al valor del atributo
victor.edad = 30
victor.sexo = "masculino"
victor.pais = "Bolivia"
maria.edad = 25
maria.sexo = "femenino"
maria.pais = "colombia"


print(victor.edad)
print(maria.edad)

#Para los metodos primero:
#Creamos la clase
class Matematica:
#iniciamos un procedimiento
    #usamos la palabra def, le damos un nombre al procedimiento y luego usamos
    #la palabra self que nos sirve para referirnos al objeto
    def suma(self):
        #usamos de nuevo la palabra self seguido de un punto y asignamos un nombre
        #para la variable que será igual a un algoritmo o valor especifico
        self.n1 = 2
        self.n2 = 3

#creamos un objeto para poder usar el metodo o procedimiento
s = Matematica()
#Debemos llamar al método o procedimiento. primero debemos llamar
#al objeto, despues un punto y despues el nombre del metodo, objeto.nombredelmetodo()
s.suma()
#Para imprimir sumanos 
#primero el nombre del objeto, despues el nombre de la variable
#que esta dentro del procedimiento o metodo
print(s.n1 + s.n2)

#CON INIT
#el init es como la palabra inicio

#creamos la clase
class Ropa:
    #iniciamos el metodo con def pero incluimos el init
    def __init__(self):
        self.marca = "lacoste"
        self.talla = "M"
        self.color = "rojo"

#Creamos un objeto
camisa = Ropa()

#imprimimos los atributos 
print(camisa.talla)
print(camisa.marca)
print(camisa.color)


#CALCULADORA
class Calculadora:
    #En este caso los atributos contendran algoritmos y no valore
    #por eso, junto al sefl ponemos el nombre de los algoritmos
    #(self,n1,n2)
    #un algoritmo es una variable
    def __init__(self,n1,n2):
        self.suma = n1 + n2 #n1 y n2 no son valores, sino son algoritmos
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

#creamos un objeto
#en los parametros no podemos dejar vacio porque 
#en este ejercicio los atributos tienen variables 
#y no valores, por eso debemos poner los valores en los parametros
operacion = Calculadora(2,3)
print(operacion.producto)
