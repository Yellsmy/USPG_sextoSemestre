import json
print("_________PERSISTENCIA DE DATOS________","\n")
data = {}
data["clientes"]=[]
data["clientes"].append({"first_name": "sigrid", "last_name": "paz", "pin": 2727, "saldo": 7.17})

data["clientes"].append({"first_name": "Jose", "last_name": "Pereira", "pin": 31, "saldo": 5.50})

data["clientes"].append({"first_name": "Luis", "last_name": "Rivera", "pin": 36, "saldo": 1.11})

with open("data_proyecto.json","w") as file:
    json.dump(data,file,indent=4)


with open("data_proyecto.json") as file:
    data = json.load(file)

    for client in data["clientes"]:
        if client["first_name"]== "Jose":
            print("first_name:", client["first_name"])
            print("last_name:", client["last_name"])
            print("pin:", client["pin"])
            print("saldo:", client["saldo"])
            print("")


print("_________POLIMORFISMO________","\n")

class animal():
    def hablar(self):
        print("Qué idioma quieres?")

class gato(animal):
    def hablar(self):
        print("MIAU")

class perro(animal):
    def hablar(self):
        print("GUAU")

def escucharMascota(animal):
    animal.hablar()

if __name__ == "__nain__":
    #instanciamos objetos
    g = gato()
    p = perro()

    #Llamamos metodos polimorficos
    g.hablar
    p.hablar
    escucharMascota(g)
    escucharMascota(p)



class Persona():
    def __init__ (self):
        self.cedula = 10939302
    def mensaje(self):
        print("mensaje desde la clase persona")

class Obrero():
    def __init__ (self):
        self.especialista = 1

    def mensaje(self):
        print("mensaje desde la clase obrero")

obrero_planta = Obrero()
obrero_planta.mensaje()


print("_________POLIMORFISMO________","\n")


