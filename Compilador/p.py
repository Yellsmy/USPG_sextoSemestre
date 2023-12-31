
import re
import analizadorSintactico
from Errores import SemanticError
variablefor = ''
class Symbol:
    def __init__(self, name, type=None, location=None):
        self.name = name
        self.type = type
        self.location = location  # Línea o posición en el código fuente

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def add(self, symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol
        if current_scope_only or self.parent is None:
            return None
        print('dentro de la revision: ', self.parent.lookup(name))
        return self.parent.lookup(name)

class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = SymbolTable()

    def declare_variable(self, var_name, var_type, location):
        if self.current_scope.lookup(var_name, current_scope_only=True):
            raise SemanticError(f"Variable '{var_name}' ya declarada.", location)
        self.current_scope.add(Symbol(var_name, var_type, location))

    def check_variable(self, var_name, location):
        symbol = self.current_scope.lookup(var_name)
        if symbol is None:
            raise SemanticError(f"Variable '{var_name}' no declarada.", location)
        return symbol.type

    def validate_assignment(self, var_name, var_type, value, location):
        print("inicio evaluacion", var_type[1], value)
        valor = str(value)
        print("valor", value)
        if var_type[1] == 'int' and not valor.isnumeric():
            print("entró")
            raise SemanticError(f"Error: La variable {var_name} es de tipo int, pero se le asigna un valor no numérico.", location)
        elif var_type[1] == 'String' and not re.match(r'^".*"$', value):
            raise SemanticError(f"Error: La variable {var_name} es de tipo String, pero el valor asignado no está entre comillas dobles.", location)
        elif var_type[1] == 'boolean' and valor.lower() not in ('true', 'false'):
            raise SemanticError(f"Error: La variable {var_name} es de tipo boolean, pero se le asigna un valor no válido.", location)
        elif var_type[1] == 'double' and not re.match(r'^-?\d+(\.\d+)?$', valor):
            raise SemanticError(f"Error: La variable {var_name} es de tipo double, pero el valor asignado no es un número válido.", location)

    def validate_for(self, name_nodo, var_name, location):
        global variablefor
        if name_nodo == 'inicializacion':
            print('dentro de la inicializacion', var_name)
            variablefor= var_name
        else:
            print('variable for', var_name)
            print('variable for', variablefor)
            if var_name != variablefor:
                raise SemanticError(f"Error: La variable {var_name} no ha sido inicializada", location)
            else: pass
                

    def list_symbols(self):
        symbols_list = []
        for name, symbol in self.current_scope.symbols.items():
            symbols_list.append((symbol.name, symbol.type, symbol.location))
        return symbols_list

    def analyze(self, node):
        
        if node is None:
            return

        if isinstance(node, tuple):
            
            print("nodo 0", node[0])
            if node[0] == 'dcl_variable' or node[0] == 'dcl_variable_with_init':
                print('name_var:',node[2] )
                self.declare_variable(node[2], node[1],node[3])
                if node[0] == 'dcl_variable_with_init':
                    self.validate_assignment(node[2], node[1], node[3], node[4])

            elif node[0] == 'array_dcl' or node[0] == 'array_usage':
                self.declare_variable(node[2], node[1],node[4])
                if node[0] == 'array_usage':
                    args = node[3]
                    for arg in args:
                        print("long", arg[0])
                    
                        self.validate_assignment(node[2], node[1], arg[0], node[4])


            elif node[0] == 'assignment':
                var_type = self.check_variable(node[1], node[3])
                print("tipo:",var_type)
                print("valor:",node[2])
                self.validate_assignment(node[1], var_type, node[2], node[3])
            
            elif node[0] == 'array_assignment':
                var_type = self.check_variable(node[1], node[3])
                self.validate_assignment(node[1], var_type, node[2], node[3])

            elif node[0] == 'inicializacion' or node[0] == 'condicion_var' or node[0] == 'increment or decrement':
                self.validate_for(node[0], node[1], node[3])
            
            elif node[0] == 'print_elemento':
                if node[1] != variablefor:
                    raise SemanticError(f"Error: La variable {node[1]} no ha sido inicializada", node[2])

            elif node[0] == 'print_lista':
                print('var:', node[1])
                if node[1] != variablefor:
                    self.check_variable(node[1], node[3])
                if node[2] != ';':
                    if node[2] != variablefor:
                        raise SemanticError(f"Error: La variable {node[2]} no ha sido declarada", node[3])

            elif node[0]== 'condicion_if':
                self.check_variable(node[1], node[3])
            

            # Continuar el análisis para los nodos hijos
            for child in node[1:]:
                self.analyze(child)

        elif isinstance(node, list):
            for child in node:
                self.analyze(child)


# Ejemplo de uso
analyzer = SemanticAnalyzer()
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



