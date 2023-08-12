import string
import re

def identificar_tokens(cadena):
    tokens = []
    regex_numero = r"[-+]?\d*\.\d+|\d+"
    regex_operadores = r"[-+*/^()]"
    
    while cadena:
        match_numero = re.match(regex_numero, cadena)
        match_operador = re.match(regex_operadores, cadena)
        
        if match_numero:
            token = match_numero.group(0)
            if '.' in token:
                tokens.append(('NUMERO_DECIMAL', float(token)))
            else:
                tokens.append(('NUMERO_ENTERO', int(token)))
            cadena = cadena[len(token):].strip()
        elif match_operador:
            tokens.append(('SIGO_' + match_operador.group(0), match_operador.group(0)))
            cadena = cadena[len(match_operador.group(0)):].strip()
        else:
            tokens.append(('ERROR', cadena[0]))
            cadena = cadena[1:].strip()
    
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
                    print(f"{tipo:<25} {valor}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
