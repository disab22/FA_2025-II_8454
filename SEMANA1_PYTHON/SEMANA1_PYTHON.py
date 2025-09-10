import math


def ejer1():
    nombre = input("Ingresa tu nombre:")
    carrera = input("Ingresa tu carrera:")

    print(f"\n{nombre},  Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}")

def ejer2():
    print("\"Allison\"")

def ejer3():
    N1=int(input("Ingrese N1: "))
    N2=int(input("Ingrese N2: "))

    print("\nSuma: ", (N1+N2))
    print("Reta: ", (N1-N2))
    print("Multi: ", (N1*N2))
    print ("Divi: ",(N1/N2))

def ejer4():
    num=float(input("Ingrese un numero decimal: "))

    raiz2 = math.sqrt(num)
    redo = round(num,0)
    cubo = math.pow(num,3)
    raiz3 = math.pow(num,1/3)

    print("\nRaiz 2: ",raiz2)
    print("Redondeado: ", redo)
    print("Al cubo: ", cubo)
    print("Raiz3: ",raiz3)

def ejer5():
    num = input("Ingrese un numero: ")

    entero = int(num)
    deci = float(num)

    print("\nResto: ", entero%2)
    print("\nDividido 3: ", deci/3)





ejer4() 

