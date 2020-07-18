import math
from classes.puntos import punto


def obtenerPuntos():
    global A
    global B
    a = input("Ingrese el punto A separando las coordenadas con comas: ").split(',')
    b = input("Ingrese el punto B separando las coordenadas con comas: ").split(',')
    A = punto(a[0], a[1])
    B = punto(b[0], b[1])


def distanciaEntrePuntos(pA, pB):
    d = math.sqrt(((int(pB.y)-int(pA.y))**2 + (int(pB.x)-int(pA.x)))**2)
    print("La distancia entre puntos es " + str(d))


def vectorEntrePuntos(pA, pB):
    ABx = int(pB.x) - int(pA.x)
    ABy = int(pB.y) - int(pA.y)
    BAx = int(pA.x) - int(pB.x)
    BAy = int(pA.y) - int(pB.y)

    print("El vector AB es: ({},{})".format(ABx, ABy))
    print("El vector BA es: ({},{})".format(BAx, BAy))


def separar():
    print("!___________________________________!")


obtenerPuntos()
separar()

A.imprimirPunto()
A.obtenerCuadrante()
A.distorigen()
A.grafico()
separar()
B.imprimirPunto()
B.obtenerCuadrante()
B.distorigen()
B.grafico()
separar()

distanciaEntrePuntos(A, B)
separar()
vectorEntrePuntos(A, B)

A.grafico()