import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    'IF',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'IDENTIFIER',
    'COMMA',
    'NUMBER',
)

# Reglas de tokens
t_IF = r'if'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_NUMBER = r'\d+'

# Reglas de tokens para identificadores
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verifica si el token es una palabra clave
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Palabras clave
reserved = {
    'if': 'IF',
}


# Reglas de análisis sintáctico
def p_statement(p):
    '''
    statement : if_statement
              | other_statement
    '''
    p[0] = p[1]

# Acciones para la producción p_if_statement
def p_if_statement(p):
    'if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE'
    print("Sentencia 'if' válida")

# Acciones para la producción p_other_statement
def p_other_statement(p):
    'other_statement : IDENTIFIER'
    p[0] = p[1]

# Acciones para la producción p_condition
def p_condition(p):
    'condition : IDENTIFIER'
    p[0] = p[1]

# Acciones para las producciones en p_statements
def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# Analizador sintáctico
parser = yacc.yacc()

# Función para leer el archivo y obtener la lista de tokens
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.readlines()

# Función para analizar los tokens del archivo
def analizar_tokens(lines):
    tokens = []
    for line in lines:
        token_data = [pair.split(': ', 1) for pair in line.strip().split(', ') if ':' in pair]
        valor = token_data[1][1]
        tokens.append(valor)
    return tokens

# Función para convertir una lista de tokens en una cadena
def tokens_to_string(tokens):
    return ' '.join(tokens)  # Esto concatena los tokens con espacios en blanco

if __name__ == '__main__':
    archivo_tokens = 'tokens_1.txt'
    lines = leer_archivo(archivo_tokens)
    tokens = analizar_tokens(lines)
    
    # Convierte la lista de tokens en una cadena
    codigo_fuente = tokens_to_string(tokens)
    
    result = parser.parse(codigo_fuente)


# Función para analizar los tokens del archivo
'''def analizar_tokens(lines):
    tokens = []
    for line in lines:
        token_data = [pair.split(': ', 1) for pair in line.strip().split(', ') if ':' in pair]
        tipo = token_data[0][1]
        valor = token_data[1][1]
        linea = int(token_data[2][1])
        tokens.append((tipo, valor, linea))
    return tokens'''