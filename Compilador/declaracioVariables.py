import re

patron = re.compile(r'^\s*([a-zA-Z_]\w*)\s+([a-zA-Z_]\w*)\s*=\s*(.+?)\s*;\s*$')


codigo_java = [
    'int numero = 4;',
    'String cadena = "Hola mundo";',
    'double valor = 3.1416;',
    'String cadenaNumerica = "123";'
]

# Valida cada declaración
for codigo in codigo_java:
    declaration = re.match(patron, codigo)
    if declaration:
        tipo_dato, nombre_variable, valor_asignado = declaration.groups()
        if tipo_dato == 'int':
            if valor_asignado and not valor_asignado.isnumeric():
                print(f"Error: La variable {nombre_variable} es de tipo int, pero se le asigna un valor no numérico.")
            else:
                print(f"La variable {nombre_variable} es correcta")
        elif tipo_dato == 'String':
            if valor_asignado and not re.match(r'^".*"$', valor_asignado):
                print(f"Error: La variable {nombre_variable} es de tipo String, pero el valor asignado no está entre comillas dobles.")
            else:
                print(f"La variable {nombre_variable} es correcta")
        elif tipo_dato == 'boolean':
            if valor_asignado and valor_asignado.lower() not in ('true', 'false'):
                print(f"Error: La variable {nombre_variable} es de tipo boolean, pero se le asigna un valor no válido.")
            else:
                print(f"La variable {nombre_variable} es correcta")
        elif tipo_dato == 'double':
            if valor_asignado and not re.match(r'^-?\d+(\.\d+)?$', valor_asignado):
                print(f"Error: La variable {nombre_variable} es de tipo double, pero el valor asignado no es un número válido.")
            else:
                print(f"La variable {nombre_variable} es correcta")
        else:
            print(f"Error: La variable {nombre_variable} tiene un tipo de dato no válido: {tipo_dato}")
    else:
        print(f"Error: La declaración no cumple con el formato esperado: {codigo}")
