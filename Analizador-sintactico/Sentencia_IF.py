
# Función para leer el archivo y obtener la lista de tokens
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.readlines()

# Función para analizar los tokens del archivo
# Función para analizar los tokens del archivo
def analizar_tokens(lines):
    tokens = []
    for line in lines:
        token_data = [pair.split(': ', 1) for pair in line.strip().split(', ') if ':' in pair]
        tipo = token_data[0][1]
        valor = token_data[1][1]
        tokens.append((tipo, valor))
    return tokens

import ply.yacc as yacc

tokens = [
    'IF',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
    'EQUALS',
    'LESS',
    'GREATER',
    'AND',
    'OR',
    'NOT',
]

# Reglas de tokens
t_IF = r'if'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_NUMBER = r'\d+'
t_OPERATOR = r'[+\-*/]'

# REGLAS DE PRODUCCIÓN



# Reglas para diferentes tipos de expresiones/condiciones
def p_expression(p):
    """
    expression : expression EQUALS expression
               | expression LESS expression
               | expression GREATER expression
               | expression AND expression
               | expression OR expression
               | NOT expression
               | IDENTIFIER
               | NUMBER
    """
    # Agrega aquí la lógica para construir la estructura de la expresión
    if len(p) == 4:
        p[0] = ("expression", p[2], p[1], p[3])
    else:
        p[0] = ("expression", p[1])


# Reglas de producción

# Regla para una única sentencia
def p_statement(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                | assignment
                | array_usage'''
    # Agrega aquí la lógica para construir la estructura de la sentencia
    if len(p) == 2:
        p[0] = ('statement', p[1])
    else:
        p[0] = ('if', p[3], p[6])

# Reglas para un conjunto de sentencias
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    # Agrega aquí la lógica para construir la estructura de statements
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# Reglas de producción

# Define la regla para una asignación
def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''
    # Agrega aquí la lógica para construir la estructura de la asignación
    p[0] = ('assignment', p[1], p[3])

# Define la regla para el uso de un arreglo (array usage)
def p_array_usage(p):
    '''array_usage : IDENTIFIER LBRACE expression RBRACE'''
    # Agrega aquí la lógica para construir la estructura del uso de un arreglo
    p[0] = ('array_usage', p[1], p[3])

# ...

# Ahora, puedes utilizar 'assignment' y 'array_usage' en otras reglas de producción según sea necesario.




# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis:", p)

lexer=''
# Crea el analizador sintáctico
parser = yacc.yacc(lexer=lexer)

def main():
    archivo_tokens = 'tokens_3.txt'
    lines = leer_archivo(archivo_tokens)
    tokens = analizar_tokens(lines)
    for token in tokens:
        print("token: ", token)
    lexer = tokens
    result = parser.parse(tokens)
    print(result)

if __name__ == "__main__":
    main()
