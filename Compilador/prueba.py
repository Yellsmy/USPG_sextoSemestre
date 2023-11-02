class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def vacia(self):
        return len(self.items) == 0

    def buscar_y_eliminar_apertura(self, char, lista_delimitadores_cierre):
        DELIMITADORES = {')': '(', '}': '{', ']': '['}
        delimitador_apertura = DELIMITADORES.get(char)
        for i, (valor, linea2) in enumerate(self.items):
            if valor == delimitador_apertura:
                self.items.pop(i)
                self.buscar_y_eliminar_cierre(char, lista_delimitadores_cierre)
                return True
        return False

    def buscar_y_eliminar_cierre(self, char, lista_delimitadores_cierre):
        for elemento in lista_delimitadores_cierre:
            valor, linea2 = elemento
            if char == valor:
                lista_delimitadores_cierre.remove(elemento)
                return True
        return False

def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.readlines()

def verificar_delimitadores(file_path,pila,lista_delimitadores_cierre):
    with open(file_path, 'r') as file:
        line_number = 0 
        for line in file:
            line_number += 1 
            for char in line:
                if char in '([{':
                    pila.push((char, line_number))
                elif char in ')]}':
                    lista_delimitadores_cierre.append((char, line_number))
                    pila.buscar_y_eliminar_apertura(char, lista_delimitadores_cierre)

def imprimir_resultado(pila, lista_delimitadores_cierre):
    if pila.vacia() and not lista_delimitadores_cierre:
        print("TODOS LOS DELIMITADORES ESTÁN CERRADOS")
        return True
    else:
        if not pila.vacia():
            print("ERROR! DELIMITADORES SIN CIERRE EN LAS SIGUIENTES LÍNEAS:")
            for delimitador, linea in pila.items:
                print(f"Línea {linea}: Delimitador '{delimitador}'")
        if lista_delimitadores_cierre:
            print("ERROR! DELIMITADORES SIN APERTURA EN LAS SIGUIENTES LÍNEAS:")
            for delimitador, linea in lista_delimitadores_cierre:
                print(f"Línea {linea}: Delimitador '{delimitador}'")
        return False

def ejecutar_verificador(archivo): 
    pila = Pila()
    lista_delimitadores_cierre = []
    verificar_delimitadores(archivo, pila, lista_delimitadores_cierre)
    return imprimir_resultado(pila, lista_delimitadores_cierre)