import math
from matplotlib import pyplot as plt


class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def imprimirPunto(self):
        print("El punto es: {}".format(self))

    def obtenerCuadrante(self):
        x = int(self.x)
        y = int(self.y)

        if x > 0 and y > 0:
            print("El punto {} se encuentra en el primer cuadrante".format(self))
        elif x < 0 and y > 0:
            print("El punto {} se encuentra en el segundo cuadrante".format(self))
        elif x < 0 and y < 0:
            print("El punto {} se encuentra en el tercer cuadrante".format(self))
        elif x > 0 and y < 0:
            print("El punto {} se encuentra en el cuarto cuadrante".format(self))
        elif x == 0 and y == 0:
            print("El punto {} se encuentra en el orígen".format(self))
        elif x == 0 and y != 0:
            print("El punto {} se encuentra sobre el eje Y".format(self))
        elif x != 0 and y == 0:
            print("El punto {} se encuentra sobre el eje X".format(self))

    def distorigen(self):
        d = math.sqrt(int(self.x)**2 + int(self.y)**2)
        print("La distancia del punto " + str(self) + " al origen es " + str(d))
        return d

    def grafico(self):
        plt.plot(self.x, self.y, marker="o", color="red")

