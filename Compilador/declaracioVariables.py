import re

patron = re.compile(r'^\s*([a-zA-Z_]\w*)\s+([a-zA-Z_]\w*)\s*=\s*(.+?)\s*;\s*$')

patron_declaration = re.compile(r'^\s*(?:[a-zA-Z_]\w*\s+)?([a-zA-Z_]\w*)\s*(=.*|;)$')


codigo_java = [
    'int numero = 4;',
    'String cadena = "Hola mundo";',
    'double valor = 3.1416;',
    'String cadenaNumerica = "123";'
]

# Valida cada declaración
def validarDeclaraciónyAsignacion(codigo_java):
    for codigo in codigo_java:
        declaration_asignacion = re.match(patron, codigo)
        declaration = re.match(patron_declaration, codigo)
        if declaration_asignacion:
            tipo_dato, nombre_variable, valor_asignado = declaration_asignacion.groups()
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
        elif declaration:
            nombre_variable = declaration.group(1)
            print(f"Declaration de la variable {nombre_variable} es correcta")
        else:
            print(f"Error: La declaración no cumple con el formato esperado: {codigo}")


def validarVariales(codigo_java):
    variables_declaradas = set()
    for codigo in codigo_java:
        match = re.match(patron_declaration, codigo)
        if match:
            nombre_variable = match.group(1)

            # Distinguir entre declaración y asignación
            if "=" in codigo:
                # Asignación: verificar si la variable ha sido declarada
                if nombre_variable not in variables_declaradas:
                    print(f"Error: La variable {nombre_variable} se utiliza antes de ser declarada.")
                    return False
            else:
                # Declaración: agregar la variable al conjunto si aún no ha sido declarada
                if nombre_variable in variables_declaradas:
                    print(f"Error: La variable {nombre_variable} ya ha sido declarada.")
                    return False
                variables_declaradas.add(nombre_variable)
        else:
            print(f"Error: La declaración no cumple con el formato esperado: {codigo}")
            return False

    print("El código es válido.")
    return True

# Ejemplos de uso  para asignacion
codigo = [
    'int numero;',
    'String cadena;',
    'String cadena = "Hola mundo";',
    'double valor = 3.1416;',
    'String cadenaNumerica = "123";'
]

validarDeclaraciónyAsignacion(codigo)

# Ejemplos de uso para declaracion
codigo_valido = [
    'int numero;',
    'numero = 20;',
    'boolea numero2;',
]

codigo_invalido = [
    'numero = 20;',
    'int numero;'
]

# Prueba con código válido
validarVariales(codigo_valido)

# Prueba con código inválido
validarVariales(codigo_invalido)