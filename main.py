from sympy import *


def getCoords():
    x1 = float(input("Entre com o valor de x1: "))
    y1 = float(input("Entre com o valor de y1: "))
    x2 = float(input("Entre com o valor de x2: "))
    y2 = float(input("Entre com o valor de y2: "))
    x3 = float(input("Entre com o valor de x3: "))
    y3 = float(input("Entre com o valor de y3: "))

    return x1, x2, x3, y1, y2, y3


def calcEquidistance(x1, x2, x3, y1, y2, y3):
    xmAB = (x1 + x2) / 2
    ymAB = (y1 + y2) / 2
    xmBC = (x3 + x2) / 2
    ymBC = (y3 + y2) / 2
    xmAC = (x3 + x1) / 2
    ymAC = (y3 + y1) / 2

    yDiffAB = y2 - y1
    xDiffAB = x2 - x1
    yDiffBC = y3 - y2
    xDiffBC = x3 - x2
    yDiffAC = y3 - y1
    xDiffAC = x3 - x1

    if yDiffAB != 0 and xDiffAB != 0:
        a = yDiffAB / xDiffAB
        a1 = -1 / a
        a2 = (ymAB) - (a1*xmAB)

    if yDiffBC != 0 and xDiffBC != 0:
        b = yDiffBC / xDiffBC
        b1 = -1 / b
        b2 = ymBC - (b1*xmBC)

    if yDiffAC != 0 and xDiffAC != 0:
        c1 = -1 / (yDiffAC / xDiffAC)
        c2 = ymAC - (c1*xmAC)

    def getResult():
        con = -b1
        con1 = -b2
        ad = con + a1
        ad1 = a2 + con1
        di = ad1 / ad
        di1 = -di
        y8 = (b1 * di1) + b2

        print("Ponto equidistante:", [di1, y8])

    if yDiffAB != 0 and xDiffAB != 0 and yDiffBC != 0 and xDiffBC != 0 and yDiffAC != 0 and xDiffAC != 0:
        getResult()

    elif yDiffAB != 0 and xDiffAB != 0 and yDiffBC != 0 and xDiffBC != 0:
        getResult()

    elif yDiffBC != 0 and xDiffBC != 0 and yDiffAC != 0 and xDiffAC != 0:
        getResult()

    elif yDiffAB != 0 and xDiffAB != 0 and yDiffAC != 0 and xDiffAC != 0:
        getResult()


x1, x2, x3, y1, y2, y3 = getCoords()
calcEquidistance(x1, x2, x3, y1, y2, y3)
