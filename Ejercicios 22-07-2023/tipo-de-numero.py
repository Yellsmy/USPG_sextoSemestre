def es_numero(cadena):
    try:
        int(cadena)
        return "entero"
    except ValueError:
        try:
            float(cadena)
            return "decimal"
        except ValueError:
            return "ninguno"

if __name__ == "__main__":
    cadena = input("Ingresa una cadena de caracteres: ")

    resultado = es_numero(cadena)
    if resultado == "entero":
        print("La cadena es un número entero.")
    elif resultado == "decimal":
        print("La cadena es un número decimal.")
    else:
        print("La cadena no es un número entero ni decimal.")