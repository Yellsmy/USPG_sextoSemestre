import re
import analizadorSintactico
from Errores import SemanticError

# Variable global para rastrear la variable usada en bucles for
variablefor = ''

# Clase que representa un símbolo en el análisis semántico
class Symbol:
    def __init__(self, name, type=None, location=None):
        self.name = name
        self.type = type
        self.location = location 

# Clase que representa la tabla de símbolos
class SymbolTable:
    def __init__(self):
        self.symbols = {} # Diccionario para almacenar símbolos
        self.parent = None 

    # Agregar un símbolo a la tabla
    def add(self, symbol):
        self.symbols[symbol.name] = symbol

    # Buscar un símbolo por nombre, primero en el ámbito actual
    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol
        
        # Si no se encuentra y se permite la búsqueda en ámbitos padres, buscar en el ámbito padre
        if current_scope_only or self.parent is None:
            return None
        return self.parent.lookup(name)

# Clase principal para el análisis semántico
class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = SymbolTable() # Inicializar con una tabla de símbolos para el ámbito global

    # Para declarar una variable y añadirla a la tabla de símbolos
    def declare_variable(self, var_name, var_type, location):
        if self.current_scope.lookup(var_name, current_scope_only=True):
            raise SemanticError(f"Variable '{var_name}' ya declarada. Línea {location}")
        self.current_scope.add(Symbol(var_name, var_type, location))

    # Verificar si una variable ha sido declarada
    def check_variable(self, var_name, location):
        symbol = self.current_scope.lookup(var_name)
        if symbol is None:
            raise SemanticError(f"Variable '{var_name}' no declarada. Línea: {location}" )
        return symbol.type

    # Validar las asignaciones a variables
    def validate_assignment(self, var_name, var_type, value, location):
        valor = str(value)
        if var_type[1] == 'int' and not valor.isnumeric():
            raise SemanticError(f"Error: La variable {var_name} es de tipo int, pero se le asigna un valor no numérico. Línea: {location}" )
        elif var_type[1] == 'String' and not re.match(r'^".*"$', value):
            raise SemanticError(f"Error: La variable {var_name} es de tipo String, pero el valor asignado no está entre comillas dobles. Línea: {location}")
        elif var_type[1] == 'boolean' and valor.lower() not in ('true', 'false'):
            raise SemanticError(f"Error: La variable {var_name} es de tipo boolean, pero se le asigna un valor no válido. Línea: {location}")
        elif var_type[1] == 'double' and not re.match(r'^-?\d+(\.\d+)?$', valor):
            raise SemanticError(f"Error: La variable {var_name} es de tipo double, pero el valor asignado no es un número válido. Línea: {location}")

    # Validar variables en bucles for
    def validate_for(self, name_nodo, var_name, location):
        global variablefor
        if name_nodo == 'inicializacion':
            variablefor= var_name # Establece la variable del bucle for
        else:
            if var_name != variablefor:
                raise SemanticError(f"Error: La variable {var_name} no ha sido inicializada.  Línea: {location}")
            else: pass
                
    # Listar todos los símbolos en la tabla de símbolos actual
    def list_symbols(self):
        symbols_list = []
        for name, symbol in self.current_scope.symbols.items():
            symbols_list.append((symbol.name, symbol.type, symbol.location))
        return symbols_list

    def analyze(self, node):
        # Analizar nodos del árbol sintáctico
        if node is None:
            return

        # Procesar diferentes tipos de nodos (declaraciones, asignaciones, etc.)
        if isinstance(node, tuple):

            if node[0] == 'dcl_variable' or node[0] == 'dcl_variable_with_init':
                self.declare_variable(node[2], node[1],node[3])
                if node[0] == 'dcl_variable_with_init':
                    self.validate_assignment(node[2], node[1], node[3], node[4])

            elif node[0] == 'array_dcl' or node[0] == 'array_usage':
                self.declare_variable(node[2], node[1],node[4])
                if node[0] == 'array_usage':
                    args = node[3]
                    for arg in args:
                        self.validate_assignment(node[2], node[1], arg[0], node[4])


            elif node[0] == 'assignment':
                var_type = self.check_variable(node[1], node[3])
                self.validate_assignment(node[1], var_type, node[2], node[3])
            
            elif node[0] == 'array_assignment':
                var_type = self.check_variable(node[1], node[3])
                self.validate_assignment(node[1], var_type, node[2], node[3])

            elif node[0] == 'inicializacion' or node[0] == 'condicion_var' or node[0] == 'increment or decrement':
                
                    self.validate_for(node[0], node[1], node[3])
            
            elif node[0] == 'print_elemento':
                if node[1] != variablefor:
                    raise SemanticError(f"Error: La variable {node[1]} no ha sido inicializada.  Línea: {node[2]}")

            elif node[0] == 'print_lista':
                if node[1] != variablefor:
                    self.check_variable(node[1], node[3])
                if node[2] != ';':
                    if node[2] != variablefor:
                        raise SemanticError(f"Error: La variable {node[2]} no ha sido declarada. Línea {node[3]}")

            elif node[0]== 'condicion_if':
                self.check_variable(node[1], node[3])
            
            # Continuar el análisis para los nodos hijos
            for child in node[1:]:
                self.analyze(child)

        # Procesar cada elemento en una lista de nodos
        elif isinstance(node, list):
            for child in node:
                self.analyze(child)

# Función para ejecutar el análisis semántico
def ejecutarSemantico(ats):
    try:
        analyzer = SemanticAnalyzer()
        analyzer.analyze(ats)
        return analyzer.list_symbols()
    except SemanticError as e:
        raise e



# Ejemplo de uso
'''analyzer = SemanticAnalyzer()
try:
    nombre_archivo = 'test.txt'
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        entrada = archivo.read()
    ats = analizadorSintactico.call_Parse(entrada)
    analyzer.analyze(ats)
    lista = analyzer.list_symbols()
    for l in lista:
        print(l)
except SemanticError as e:
    print(f"Error semántico: {e} en la línea {e.location}")



'''