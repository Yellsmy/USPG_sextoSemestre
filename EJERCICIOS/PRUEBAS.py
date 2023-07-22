"""
def print_full_name(first,last):
    if len(first) <= 10:
        if len(last) <= 10:
            print("Hola {} {} Acabas de profundizar en python".format(first_name,last_name))

if __name__ == "__main__":
    first_name = input()
    last_name = input()
    print_full_name(first_name,last_name)"""


"""def split_and_join(línea):
    línea = línea.split(" ")
    print(línea)
    línea = "-".join(línea)
    print(línea)
    return línea

if __name__ == "__main__":
    línea = input()
    resultado = split_and_join(línea)
    print(resultado)"""

"""def mutate_string(string,position,character):
    lista = list(string)
    lista[position]= character
    string = "".join(lista)
    return string

if __name__ == "__main__":
    s = input()
    i,c = input()
    s_new = mutate_string(s, int(i),c)
    print(s_new)"""


"""def swap_case(s):
    return s.swapcase()

if __name__ == "__main__":
    s = input()
    resultado = swap_case(s)
    print(resultado)"""

def minion_game(string):
    # your code goes here
    if len(string) <= 10**6 and len(string) > 0:
        string_U = string.upper()
        jugador1= 0
        jugador2= 0
        for i in range(0,len(string)):
            if string_U[i] == "A" or string_U[i] == "E" or string_U[i] == "I" or string_U[i] == "O" or string_U[i] == "U" :
                jugador2 += len(string_U) - i
            else:
                jugador1 += len(string_U) - i
        if jugador1 > jugador2:
            print("Stuart {}".format(jugador1))
        elif jugador2 > jugador1:
            print("Kevin {}".format(jugador2))
        else:
            print("Draw")

if __name__=="__main__":
    s = input()
    minion_game(s)

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self. imaginary + no.imaginary
        return Complex(real,imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real,imaginary)
        
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real,imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print ("\n".join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))