import ply.lex as lex
import ply.yacc as yacc 

# Definición de tokens
tokens = [
    'FOR',
    'LPAREN',
    'SEMICOLON',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'NUMERIC',
    'GT',
    'LT',
    'GE',
    'LE',
    'EQ',
    'NEQ',
    'PRINT',
    'STRING',
    'INT',
    'EQUALS',
    'IDENTIFIER',
    'INCREMENT'
]

palabras_reservadas = {
    'for' : 'FOR',
    'int' : 'INT',
    'print' : 'PRINT',
}

tokens += list(palabras_reservadas.values())


# Expresiones regulares para tokens
t_FOR = r'for'
t_LPAREN = r'\('
t_SEMICOLON = r';'
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_NUMERIC = r'\d+'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NEQ = r'!='
t_PRINT = r'print'
t_STRING = r'"[^"]*"'
t_INT = r'int'
t_EQUALS = r'='
t_INCREMENT = r'\+\+'

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = palabras_reservadas.get(t.value, "IDENTIFIER")  
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()


# Definición de la gramática
def p_for_statement(p):
    'for_statement : FOR LPAREN for_initial SEMICOLON condition SEMICOLON for_update RPAREN LBRACE body RBRACE'
    print("Sentencia for válida")

def p_for_initial(p):   
    'for_initial : INT IDENTIFIER EQUALS NUMERIC'
    # Ejemplo: int i = 0;

def p_for_update(p):
    'for_update : IDENTIFIER INCREMENT'
    # Ejemplo: i++;

def p_condition(p):
    '''condition :  expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression EQ expression
                 | expression NEQ expression'''

def p_expression(p):
    '''expression : NUMERIC
                  | IDENTIFIER'''


def p_body(p):
    '''body : PRINT LPAREN STRING RPAREN SEMICOLON
            | PRINT LPAREN NUMERIC RPAREN SEMICOLON'''

def p_error(p):
    print(f"Error de sintaxis en la línea {p.lineno}")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Función para evaluar una cadena de entrada
def evaluar_cadena(input_string):
    parser.parse(input_string)

input_string = input("Ingrese una sentencia for: ")
evaluar_cadena(input_string)