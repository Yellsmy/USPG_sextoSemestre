
import re

# Patrón de declaración de variable en Java
pattern = r'\b(\w+)\s+(\w+)\s*(?:=\s*([^;]+))?;'

# Código fuente Java de ejemplo
java_code = """
numero int = 4;
String cadena = "Hola mundo";
double valor = 3.14;
String cadenaNumerica = "123"
"""

# Encuentra todas las declaraciones de variables en el código Java
declarations = re.findall(pattern, java_code)

# Valida cada declaración
for declaration in declarations:
    tipo_dato, nombre_variable, valor_asignado = declaration
    if tipo_dato == 'int':
        if valor_asignado is not None and not valor_asignado.isnumeric():
            print(f"Error: La variable {nombre_variable} es de tipo int, pero se le asigna un valor no numérico.")
        else:
            print(f"La variable {nombre_variable} es correcta")
    elif tipo_dato == 'String':
        if valor_asignado is not None and not re.match(r'^".*"$', valor_asignado):
            print(f"Error: La variable {nombre_variable} es de tipo String, pero el valor asignado no está entre comillas dobles.")
        else:
            print(f"La variable {nombre_variable} es correcta")
    elif tipo_dato == 'boolean':
        if valor_asignado is not None and valor_asignado.lower() not in ('true', 'false'):
            print(f"Error: La variable {nombre_variable} es de tipo boolean, pero se le asigna un valor no válido.")
        else:
            print(f"La variable {nombre_variable} es correcta")
    elif tipo_dato == 'double':
        if valor_asignado is not None and not re.match(r'^-?\d+(\.\d+)?$', valor_asignado):
            print(f"Error: La variable {nombre_variable} es de tipo double, pero el valor asignado no es un número válido.")
        else:
            print(f"La variable {nombre_variable} es correcta")
    else:
        print(f"Error: La variable {nombre_variable} tiene un tipo de dato no válido: {tipo_dato}")
