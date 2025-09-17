from traceback import print_tb


def ejer1():
    edad= int(input("Ingrese su edad:"))

    if edad>18:
        print("Menor de edad")
    elif edad <=64:
        print("Adulto")
    else:
        print("Adulto mayor")

def ejer2():
    an=int(input("Ingrese el año: "))

    if (an % 4 == 0 and an%100 != 0) or an % 400 == 0:
        print("El año es bisiestro")
    else:
        print("El año no es bisiestro")

    if (an%2 == 0):
        print("El año es par")
def ejer3():
    monto=float(input("Ingrese monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion = (input("Ingrese una opcion: "))

    print()
    match opcion: 
        case 1:print("Dolares: ", round((monto/3.75),2))
        case 2:print("Euros: ", monto/4.05)
        case _: print("Opcion incorrecta!")
import math
def ejer4():
    print("Bienvenidos al programa de desarollo de areas\n")

    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion=int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            lado=int(input("Ingrese lado: "))
            print("Area de cuadrado: ", lado*lado)
        case 2:
            baase=int(input("Ingrese la base: "))
            alt=int(input("Ingrese la altura: "))
            print("Area de rectangulo: ", baase*alt)
        case 3:
            baase2=int(input("Ingrese la base: "))
            alt2=int(input("Ingrese la altura: "))
            print("Area de triangulo: ", (baase2*alt2)/2)
        case 4:
            rad=float(input("Ingrese el radio: "))
            print("Area del cilculo: ", round((math.pi * rad**2),2))
        case _: print("Opcion incorrecta!")
        

ejer1()