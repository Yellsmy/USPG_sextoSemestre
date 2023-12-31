#Programa que  lea un archivo el cual contiene 4.456 * (5 + 6.879 * (8 / 2^3)-7)-1 y
#muestra una salida con lista de tokens idenficados
#Realizado por Roberto Castillo y Yellsmy Toj
import string
import re

def contar_lineas(contenido):
    lineas = contenido.count('\n') + 1
    return lineas

def identificar_tokens(archivo):
    tokens = []
    token_numeros = r"[-+]?\d*\.\d+|\d+"
    token_operadores = {'*': 'SIGNO_MULTIPLICACION', '+': 'SIGNO_SUMA', '/': 'SIGO_DIVISION', '-': 'SIGNO_RESTA'}
    token_signos = {'(': 'PARENTESIS_IZQ', ')': 'PARENTESIS_DERCH', '^': 'ACENTO_CIRCUNFLEJO'}

    signos_key = token_signos.keys()
    operadores_key = token_operadores.keys()
    
    lineas = archivo.split('\n')
    for numero_linea, linea in enumerate(lineas, start=1):
        for linea in lineas:
            palabras = re.findall(r"[\w.]+|[^\s\w]", linea)
            for palabra in palabras:
                match_numero = re.match(token_numeros, palabra)
                if match_numero:
                    token = match_numero.group(0)
                    if '.' in token:
                        tokens.append(('NUMERO_DECIMAL', float(token)))
                    else:
                        tokens.append(('NUMERO_ENTERO', int(token)))
                elif palabra in operadores_key:
                    tokens.append((token_operadores[palabra], palabra))
                elif palabra in signos_key:
                    tokens.append((token_signos[palabra], palabra))
                else:
                    tokens.append(('ERROR. DATO NO VÁLIDO', palabra))
    
    return tokens

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de texto: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            tokens = identificar_tokens(contenido)

            for tipo, valor in tokens:
                if tipo == 'NUMERO_DECIMAL':
                    print(f"{tipo:<25} {valor:.3f}")
                else:
                    print(f"{tipo:<25} {valor:<15}")

            lineas= contar_lineas(contenido)
            print(f"El archivo '{nombre_archivo}' tiene {lineas} líneas")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")



