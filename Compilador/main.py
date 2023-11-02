''' 
Compilador
Fase 1 y 2
10 de octubre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''
import os
import sys
from analizadorLexico import lexer, ejecutar
from analizadorSintactico import call_Parse
from Verificador_delimitadores import ejecutar_verificador

# Crea el nombre del nuevo archivo para almacenar los tokens
def nombre__crear_archivo():
    contador = 1
    while True:
        nombre_archivo = f"tokens_{contador}.txt"
        if not os.path.exists(nombre_archivo):
            break
        contador += 1
    return nombre_archivo

# Almacena y muestra los tokens
def almacenar_ver_tokens(codigo):
    tokensValidos = ejecutar(codigo)
    guardar_archivo = input("¿Desea almacenar los tokens válidos en un archivo? (Sí/No): ")
    if guardar_archivo.lower() == "si" or guardar_archivo.lower() == "s":
        nombre_archivo= nombre__crear_archivo()
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for token in tokensValidos:
                    archivo.write(f"{token}\n")
                print(f"Los tokens se han almacenado en el archivo '{nombre_archivo}'.")
            archivo.close()
        except Exception as e:
            print(f"Ocurrió un error al almacenar los tokens en el archivo: {e}")

    imprimir = input("¿Desea ver los tokens válidos almacenados? (Si/No): ")
    if imprimir.lower() == "si" or imprimir.lower() == "s":
        for token in tokensValidos:
            print(token)

def main():
    try:
        print('¡BIENVENIDO!')
        nombre_archivo = input("Ingresa el nombre del archivo de código que quieres analizar: ")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            entrada = archivo.read()
        almacenar_ver_tokens(entrada)
        aSintactico = input("¿Desea ejecutar el analizador sintáctico?: (Si/No)")
        if aSintactico.lower() == "si" or aSintactico.lower() == "s":
            lexer.lineno = 1
            if not ejecutar_verificador(nombre_archivo):
                sys.exit(1)
            call_Parse(entrada)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Ocurrió un error al analizar el archivo: {e}")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAnálisis de tokens interrumpido por el usuario.")
