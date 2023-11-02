class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Ejemplo de uso
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print("Tamaño de la pila:", pila.size())
print("Elemento en el tope de la pila:", pila.peek())

while not pila.is_empty():
    item = pila.pop()
    print("Elemento retirado de la pila:", item)
