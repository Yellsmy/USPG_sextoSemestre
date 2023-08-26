import re


def disparador_errores(token, numero_linea):
    print("entré a la función")
    print(token)
    if token.count('.') > 2:
        print(f'ERROR. EL VALOR {token} ENCONTRADO EN LA LÍNEA {numero_linea} ES INVÁLIDO ')
        return True
    return False

def identificar_tokens(codigo):
    palabras_clave = {'while', 'if', 'return', 'cout', 'cin', 'do'}
    operadores_aritmeticos = {'+', '-', '*', '/', '%'}
    operadores_logicos = {'&&', '||', '>', '<', '==', '!='}
    simbolos_especiales = {'(', ')', '[', ']', '{', '}'}
    
    tokens_palabras_clave = []
    tokens_identificadores = []
    tokens_operadores = []
    tokens_operadores_lógicos = []
    tokens_simbolos_especiales = []

    lineas = codigo.split('\n')
    for numero_linea, linea in enumerate(lineas, start=1):
        palabras = re.findall(r"[\w]+(?:\.[\w]+)*|[^\s\w]", linea)
        for palabra in palabras:
            if disparador_errores(palabra, numero_linea):
                continue
            if re.match(r"^[a-zA-Z_]\w*$", palabra):
                tokens_identificadores.append((palabra, numero_linea))
            elif palabra in palabras_clave:
                tokens_palabras_clave.append((palabra, numero_linea))
            elif palabra in operadores_aritmeticos:
                tokens_operadores.append((palabra, numero_linea))
            elif palabra in operadores_logicos:
                tokens_operadores_lógicos.append((palabra, numero_linea))
            elif palabra in simbolos_especiales:
                tokens_simbolos_especiales.append((palabra, numero_linea))
    
    return tokens_palabras_clave, tokens_identificadores, tokens_operadores, tokens_operadores_lógicos, tokens_simbolos_especiales

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de código: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            entrada = archivo.read()

            palabras_claves, identificadores, operadores, operadores_logicos, simbolos_especiales = identificar_tokens(entrada)

            print(f"Palabras Clave: {palabras_claves}")
            print(f"Identificadores: {identificadores}")
            print(f"Operadores Aritméticos: {operadores}")
            print(f"Operadores Lógicos: {operadores_logicos}")
            print(f"Símbolos Especiales: {simbolos_especiales}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")



    def disparador_errores(self, token, numero_linea):
        estado = 0
        print("Entré a la función")
        print(token)
        if token.count('.') > 1:
            print(f'ERROR. EL VALOR {token} ENCONTRADO EN LA LÍNEA {numero_linea} ES INVÁLIDO ')
            estado = 2
        return estado
    
