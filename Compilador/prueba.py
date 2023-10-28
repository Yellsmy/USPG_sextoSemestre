import re

def validar_cadena(cadena):
    # Definir el patrón para la declaración de variables
    patron = re.compile(r'^\s*([a-zA-Z_]\w*)\s+([a-zA-Z_]\w*)\s*=\s*(.+?)\s*;\s*$')

    # Intentar hacer coincidir el patrón con la cadena de entrada
    coincidencia = patron.match(cadena)

    if coincidencia:
        tipo, nombre, valor = coincidencia.groups()

        # Verificar si el valor es numérico (int o float)
        if tipo in ('int', 'double') and not re.match(r'^[+-]?\d+(\.\d+)?$', valor):
            return False

        # Verificar si el valor es una cadena (char)
        if tipo == 'char' and not re.match(r'^".*"$', valor):
            return False

        return True
    else:
        return False

# Ejemplos
cadenas_ejemplo = [
    "int variable = 10;",
    'char contenido = "a";',
    'double valor = 10.5;',
    'int variable = "Carlos";',
    'variable int = 10;',
    'char contenido = "nuevo elemento";',
    'double valor = "nuevo"'
]

for cadena in cadenas_ejemplo:
    if validar_cadena(cadena):
        print(f'Valido: {cadena}')
    else:
        print(f'No Valido: {cadena}')