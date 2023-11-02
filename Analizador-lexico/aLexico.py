import os
import ply.lex as lex

# Lista de nombres de tokens.
tokens = [
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULUS",
    "AND",
    "OR",
    "NOT",
    "EQUALS",
    "LESS",
    "GREATER",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "SEMICOLON",
    "COMMA",
    "PERIOD",
    "QUOTE",
    "ID",
    "CLASS",
    "PUBLIC",
    "STATIC",
    "VOID",
    "MAIN",
    "STRING",
    "INT",
    "BOOLEAN",
    "TRUE",
    "FALSE",
]

# Palabras clave de Java
reserved = {
    "class": "CLASS",
    "public": "PUBLIC",
    "static": "STATIC",
    "void": "VOID",
    "main": "MAIN",
    "String": "STRING",
    "int": "INT",
    "boolean": "BOOLEAN",
    "true": "TRUE",
    "false": "FALSE",
}

tokens += list(reserved.values())

# Reglas de expresión regular para tokens simples
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_MODULUS = r"\%"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_NOT = r"\!"
t_EQUALS = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_SEMICOLON = r"\;"
t_COMMA = r"\,"
t_PERIOD = r"\."
t_QUOTE = r"\""


# Regla para identificar números enteros o decimales
def t_NUMBER(t):
    r"\d+(\.\d+)?"
    if "." in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


# Regla para identificar identificadores (variables, nombres de métodos, etc.)
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")  # Verificar si es una palabra clave
    return t


# Regla para manejar comentarios de una sola línea
def t_COMMENT(t):
    r"\/\/.*"
    pass


# Regla para manejar comentarios de bloque
def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    pass


# Regla para manejar saltos de línea y contar números de línea
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Ignorar espacios y tabulaciones
t_ignore = " \t"

# Regla para manejo de errores
def t_error(t):
    print("Carácter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()


def tokenize(data):
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)



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
    
    

# Ejemplo de uso
if __name__ == "__main__":
    try:
        nombre_archivo = input("Ingresa el nombre del archivo de código: ")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            entrada = archivo.read()
            tokenize(entrada)
    except FileNotFoundError:
            print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
    except Exception as e:
            print(f"Ocurrió un error al analizar el archivo: {e}")
    data = """
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, world!");
        }
    }
    """
    
