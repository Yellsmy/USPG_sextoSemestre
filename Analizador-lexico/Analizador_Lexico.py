'''
Compiladores
Analizador Léxico para el lenguaje de programación Java
18 de septiembre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

import os
import re
import sys
import unicodedata 

class ManejoArchivos:
    @staticmethod
    # Crea un nuevo archivo y almacena los tokens encontrados en el archivo creado
    def guardar_tokens_en_archivo(tokens):
        contador = 1
        while True:
            nombre_archivo = f"tokens_{contador}.txt"
            if not os.path.exists(nombre_archivo):
                break
            contador += 1

        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for token in tokens:
                    tipo, palabra, numero_linea = token
                    archivo.write(f"Tipo: {tipo}, valor: {palabra}, Línea: {numero_linea}\n")
            print(f"Los tokens se han almacenado en el archivo '{nombre_archivo}'.")

        except Exception as e:
            print(f"Ocurrió un error al almacenar los tokens en el archivo: {e}")
    
    # Lee el archivo que se analizará y llama a las funciones necesarias para analizarlo
    def archivo_analizado(self):
        try:
            nombre_archivo = input("Ingresa el nombre del archivo de código: ")
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                entrada = archivo.read()

                analizador_tokens = AnalizadorTokens()
                analizador = Analizador(analizador_tokens)
                tokens_validos = analizador.validar(entrada)

                guardar_archivo = input("¿Desea almacenar los tokens válidos en un archivo? (Sí/No): ")
                imprimir = 'si'
                if guardar_archivo.lower() == "si" or guardar_archivo.lower() == "s":
                    self.guardar_tokens_en_archivo(tokens_validos)
                    imprimir = input("¿Desea ver los tokens válidos almacenados? (Sí/No): ")
                if imprimir.lower() == "si" or imprimir.lower() == "s":
                    for token in tokens_validos:
                        tipo, palabra, numero_linea = token
                        print(f"Tipo: {tipo}, valor: {palabra}, Línea: {numero_linea}")
                

        except FileNotFoundError:
            print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
        except Exception as e:
            print(f"Ocurrió un error al analizar el archivo: {e}")



# Clase para analizar y almacenar cada token en la lista de tokens válidos
class Analizador:
    def __init__(self, token_analizado):
        self.token_analizado = token_analizado

    def validar(self, codigo_fuente):
        tokens_validos = []
        lineas = codigo_fuente.split('\n')
        for numero_linea, linea in enumerate(lineas, start=1):
            palabras  = re.findall(r"[\w]+(?:\.[\w]+)*|@[\w]+|\d+\.\d+|\d+|'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\"|//.*|/\*.*?\*/|>>>|&&|\|\||>=|<=|==|!=|[-+*/%&|^<>]=|<<=|>>=|[^\s\w]", linea)


            for palabra in palabras:
                try:
                    tipo = self.token_analizado.determinar_tipo_token(palabra)
                    if '"' in palabra or "'" in palabra:
                    # Token es una cadena, así que almacénala como tal
                        tokens_validos.append(('CADENA', palabra[1:-1], numero_linea))

                    elif self.token_analizado.disparador_errores(palabra, numero_linea):
                        break
                    elif "." in palabra:
                        subtokens = palabra.split(".")
                        for subtoken in subtokens:
                            tipo2 = self.token_analizado.determinar_tipo_token(subtoken)
                            tokens_validos.append((tipo2, subtoken, numero_linea))
                            if subtoken != subtokens[-1]:
                                tokens_validos.append(('DELIMITADOR', '.', numero_linea))
                    elif tipo == 'DESCONOCIDO':
                            print(f'NO SE RECONOCIÓ EL VALOR {palabra} EN LA LÍNEA {numero_linea}')
                            sys.exit(1) 
                    else:
                        tokens_validos.append((tipo, palabra, numero_linea))
                
                except Exception as e:
                    print(f"Ocurrió un error al analizar el token '{palabra}': {e}")

        return tokens_validos

# Clase para analizar los tokens y determinar su tipo
class AnalizadorTokens:
    def __init__(self):
        self.palabras_reservadas = {
            'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extends', 'false', 'final', 'finally', 'float', 'for', 'future',
            'generic', 'goto', 'if', 'implements', 'import', 'inner', 'instanceof', 'int', 'interface', 'long', 'native',
            'new', 'null', 'operator', 'outer', 'package', 'private', 'protected', 'public', 'rest', 'return', 'short',
            'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 'threadsafe', 'throw', 'throws', 'transient',
            'true', 'try', 'var', 'void', 'volatile', 'while', 'main',  'println', 'List',
            'ArrayList', 'add'
        }

        self.operadores = ['+', '-', '*', '/', '%', '\\', '=', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=', '>>>=', '++', '--', '~', '^', '<<', '>>']

        self.condicionales = {'&&', '||', '>', '<', '>=', '<=', '==', '!=', '!', '&', '|', '?'}
        self.delimitadores = {'(', ')', '[', ']', '{', '}', ';', ',', '.', '"', ':'}
        self.comentarios = [
            re.compile(r'^\s*//.*$'),
            re.compile(r'^\s*/\*.*?\*/', re.DOTALL),
            re.compile(r'^\s*/\*\*.*?\*/', re.DOTALL)
        ]
        self.anotaciones = {'@FunctionalInterface', '@SuppressWarnings', '@Target', '@Inherited', '@Documented', '@Retention',
                            '@FunctionalInterface', '@SafeVarargs', '@SuppressWarnings', '@Deprecated', '@Override'}


    # Valida que cada token cumpla con las normas, caso contrario finaliza el programa y muestra el error
    def disparador_errores(self, token, numero_linea):
        if token.count('.') > 1 and re.match(r"^\d+\.\d+\.\d+$", token):
            print(f'ERROR. EL VALOR {token} ENCONTRADO EN LA LÍNEA {numero_linea} ES INVÁLIDO ')
            sys.exit(1)
        elif re.match(r"^\d+[a-zA-Z_$][\w$]*$", token):
            print(f'ERROR. EL VALOR "{token}" EN LA LÍNEA {numero_linea} COMIENZO CON UN NÚMERO')
            sys.exit(1)
         # Nota: Verificar cuáles palabras pueden iniciar con mayúscula y cuáles no
        elif token.lower() in self.palabras_reservadas and token != token.lower():
            print(f'ERROR. LA PALABRA RESERVADA "{token}" ENCONTRADA EN LA LÍNEA {numero_linea} ESTÁ ESCRITA INCORRECTAMENTE.')
            sys.exit(1)
        elif "ñ" in token.lower():
            print(f'ERROR. El identificador "{token}" en la línea {numero_linea} es inválido')
            sys.exit(1)
        elif any(unicodedata.category(c) == "Mn" for c in unicodedata.normalize('NFD', token)):
            print(f'ERROR. El identificador "{token}" en la línea {numero_linea} contiene tildes o diacríticos y es inválido')
            sys.exit(1)
        else:
            return False

    def determinar_tipo_token(self, palabra):
        if palabra in self.palabras_reservadas:
            return 'PALABRA_RESERVADA'
        elif re.match(r"^[a-zA-Z_$][a-zA-Z0-9_$]*$", palabra) and palabra.lower() not in self.palabras_reservadas:
            return 'IDENTIFICADOR'
        elif palabra in self.operadores:
            return 'OPERADOR'
        elif palabra in self.delimitadores:
            return 'DELIMITADOR'
        elif palabra in self.condicionales:
            return 'CONDICION'
        elif any(patron.match(palabra) for patron in self.comentarios):
            return 'COMENTARIO'
        elif palabra in self.anotaciones:
            return 'ANOTACION'
        elif re.match(r"^\d+(\.\d+)?$", palabra):
            return  'NUMERO'
        else:
            return 'DESCONOCIDO'

    

if __name__ == "__main__":
    analyzer = ManejoArchivos()
    try:
        analyzer.archivo_analizado()
    except KeyboardInterrupt:
        print("\nAnálisis de tokens interrumpido por el usuario.")
