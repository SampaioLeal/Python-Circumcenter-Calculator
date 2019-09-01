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
        a = -1 / (yDiffAB / xDiffAB)
        a1 = ymAB - (a*xmAB)

    if yDiffBC != 0 and xDiffBC != 0:
        b = -1 / (yDiffBC / xDiffBC)
        b1 = ymBC - (b*xmBC)

    if yDiffAC != 0 and xDiffAC != 0:
        c = -1 / (yDiffAC / xDiffAC)
        c1 = ymAC - (c*xmAC)

    if yDiffAB != 0 and xDiffAB != 0 and yDiffBC != 0 and xDiffBC != 0 and yDiffAC != 0 and xDiffAC != 0:
        resultX = -((a1 + (-b1)) / ((-b) + a))
        resultY = (b * resultX) + b1

        print("\nPonto equidistante:", [resultX, resultY])

    elif yDiffAB != 0 and xDiffAB != 0 and yDiffBC != 0 and xDiffBC != 0:
        resultX = -((a1 + (-b1)) / ((-b) + a))
        resultY = (b * resultX) + b1

        print("\nPonto equidistante:", [resultX, resultY])

    elif yDiffBC != 0 and xDiffBC != 0 and yDiffAC != 0 and xDiffAC != 0:
        resultX = -((b1 + (-c1)) / ((-c) + b))
        resultY = (c * resultX) + c1

        print("\nPonto equidistante:", [resultX, resultY])

    elif yDiffAB != 0 and xDiffAB != 0 and yDiffAC != 0 and xDiffAC != 0:
        resultX = -((c1 + (-a1)) / ((-a) + c))
        resultY = (a * resultX) + a1

        print("\nPonto equidistante:", [resultX, resultY])


x1, x2, x3, y1, y2, y3 = getCoords()
calcEquidistance(x1, x2, x3, y1, y2, y3)
