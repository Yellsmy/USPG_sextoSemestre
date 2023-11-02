import json
#implementacion de metodos heredados de la clase abstracta 
from MisClases.AbstBaseData import ConceptAbstracBaseData

class ManagerFunction(ConceptAbstracBaseData):
  #definicion de contructor 
    def _init_(self):
      #matriz almacena el nodo Cuenta habientes 
      self.data = {}
      self.data ["CuentaHabiente"] = []
    #creamos una estructura iniciadora para una integracion continua de la misma estructura evitando asi que el resto encuentre posiciones vacias y generando una continuidad de registros 
    def CreatorUserDataBase(self):
      self.data ["CuentaHabiente"].append({
            "nombre" :"Admin", 
            "primer_apellido" :"Banking",
            "pin" : "Admin12345",
            "saldo" : "Nan"})
      with open("DataBase.json", "a") as file:
        json.dump(self.data, file, indent=4)   
    #crespetando la lectura y estructura de clave valor de nuestro archivo json podemos integrar el metodo escribir documento atraves de la funcion de asignacion 
    def SetterUserData(self,UserName,UserLastName,Password,Money):
      with open("DataBase.json")as file:
        self.data=json.load(file)
        self.data ["CuentaHabiente"].append({
            "nombre" : UserName, 
            "primer_apellido" :UserLastName,
            "pin" : Password,
            "saldo" : Money})
      with open("DataBase.json", "w") as file:
        json.dump(self.data, file, indent=4)      

    def GetterUserData(self):
      with open("DataBase.json")as file:
        self.data=json.load(file)
      for cliente in self.data["CuentaHabiente"]:
        print(cliente["nombre"])
#respetando la lectura y estructura de clave valor de nuestro archivo json podemos sobre escribir los valores de un registro siempre y cuando este sea verificado con un registro existente 
    def updateJsonFile(self,nobreDato,contraseDatos,saldo):
        jsonFile= open("DataBase.json", "r") 
        self.data = json.load(jsonFile)
        jsonFile.close() 
        
        for cliente in self.data["CuentaHabiente"]:
          if cliente["nombre"]==nobreDato and cliente["pin"]==contraseDatos :
            NewName=input("ingrese su nuevo Nombre > ")
            NewLastName=input("ingrese su nuevo Apellido > ")
            NewPin=int(input("ingrese su nuevo pin > "))
            cliente["nombre"] = NewName
            cliente["primer_apellido"]=NewLastName
            cliente["pin"] = NewPin
            cliente["saldo"]=saldo
        
        jsonFile = open("DataBase.json", "w")
        jsonFile.write(json.dumps(self.data,indent=4))
        jsonFile.close()
        print("Actualizacion completada ")
#implementacion de metodo actualizar tras primera validacion de datos 
    def UseData(self,Nombre,contrs):
      nobreDato=""
      contraseDatos=0
      with open("DataBase.json")as file:
        self.data=json.load(file)
      for cliente in self.data["CuentaHabiente"]:
          if cliente["nombre"]==Nombre and cliente["pin"]==contrs :
            nobreDato=Nombre
            contraseDatos=contrs
            ManagerFunction.updateJsonFile(self,nobreDato,contraseDatos,cliente["saldo"])