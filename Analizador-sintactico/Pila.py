'''
Compiladores
Parte 1 Analizador Sintactico
22 de septiembre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def vacia(self):
        return len(self.items) == 0

    def buscar_y_eliminar_apertura(self, token, lista_delimitadores_cierre):
        DELIMITADORES = {')': '(', '}': '{', ']': '['}
        delimitador_cierre, linea = token
        delimitador_apertura = DELIMITADORES.get(delimitador_cierre)
        for i, (valor, linea2) in enumerate(self.items):
            if valor == delimitador_apertura:
                self.items.pop(i)
                self.buscar_y_eliminar_cierre(token, lista_delimitadores_cierre)
                return True
        return False

    def buscar_y_eliminar_cierre(self, token, lista_delimitadores_cierre):
        valor, linea = token
        for elemento in lista_delimitadores_cierre:
            valor2, linea2 = elemento
            if valor == valor2:
                lista_delimitadores_cierre.remove(elemento)
                return True
        return False

def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.readlines()

def analizar_tokens(lines):
    tokens = []
    for line in lines:
        token_data = [pair.split(': ', 1) for pair in line.split(', ') if ':' in pair]
        for clave, valor in token_data:
            if clave == 'Tipo' and valor == 'DELIMITADOR':
                valor = token_data[1][1]
                linea = int(token_data[2][1])
                tokens.append((valor, linea))
    return tokens

def verificar_delimitadores(tokens, pila, lista_delimitadores_cierre):
    for token in tokens:
        valor, linea = token
        if valor in '({[':
            pila.push((valor, linea))
        elif valor in ')}]':
            lista_delimitadores_cierre.append((valor, linea))
            pila.buscar_y_eliminar_apertura(token, lista_delimitadores_cierre)
            

def imprimir_resultado(pila, lista_delimitadores_cierre):
    if pila.vacia() and not lista_delimitadores_cierre:
        print("TODOS LOS DELIMITADORES ESTÁN CERRADOS")
    else:
        if not pila.vacia():
            print("ERROR! DELIMITADORES SIN CIERRE EN LAS SIGUIENTES LÍNEAS:")
            for delimitador, linea in pila.items:
                print(f"Línea {linea}: Delimitador '{delimitador}'")
        if lista_delimitadores_cierre:
            print("ERROR! DELIMITADORES SIN APERTURA EN LAS SIGUIENTES LÍNEAS:")
            for delimitador, linea in lista_delimitadores_cierre:
                print(f"Línea {linea}: Delimitador '{delimitador}'")


def main():
    archivo_tokens = 'tokens_1.txt'
    lines = leer_archivo(archivo_tokens)
    tokens = analizar_tokens(lines)
    pila = Pila()
    lista_delimitadores_cierre = []
    verificar_delimitadores(tokens, pila, lista_delimitadores_cierre)
    imprimir_resultado(pila, lista_delimitadores_cierre)

if __name__ == "__main__":
    main()
