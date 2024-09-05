import sys


def obtener_token(input):
    if input == '+':
        return "SUMA"
    elif input == '++':
        return "INCR"
    elif es_entero(input):
        return "ENTERO"
    elif es_real(input):
        return "REAL"
    else:
        return "No se ha reconocido el token"


def es_entero(input):
    if input.isdigit():
        return True
    return False


def es_real(input):
    enteros = input.split('.')
    if len(enteros) == 2:
        if es_entero(enteros[0]) and es_entero(enteros[1]):
            return True
    return False


def main():
    if len(sys.argv) != 2:
        print("Uso: python punto1AFD.py <expresion>")
        sys.exit(1)

    expresion = sys.argv[1]

    token = obtener_token(expresion)

    print(token)


if __name__ == "__main__":
    main()
