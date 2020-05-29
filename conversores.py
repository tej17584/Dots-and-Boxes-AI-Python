#este python es para funciones utiles
""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: conversores.py
Propósito: este es un conversor de coordenadas """


# ? método para convertir de valor tablero a Coordenada
def fromBoardToCoordenate(primero, segundo):
    coorX = -5
    coorY = -5
    if (primero == 0):
        if (segundo == 0 or segundo == 5 or segundo == 10 or segundo == 15 or segundo == 20 or segundo == 25):
            coorX = 1
            if segundo == 0:
                coorY = 0
            elif segundo == 5:
                coorY = 2
            elif segundo == 10:
                coorY = 4
            elif segundo == 15:
                coorY = 6
            elif segundo == 20:
                coorY = 8
            elif segundo == 25:
                coorY = 10
        elif(segundo == 1 or segundo == 6 or segundo == 11 or segundo == 16 or segundo == 21 or segundo == 26):
            coorX = 3
            if segundo == 1:
                coorY = 0
            elif segundo == 6:
                coorY = 2
            elif segundo == 11:
                coorY = 4
            elif segundo == 16:
                coorY = 6
            elif segundo == 21:
                coorY = 8
            elif segundo == 26:
                coorY = 10
        elif(segundo == 2 or segundo == 7 or segundo == 12 or segundo == 17 or segundo == 22 or segundo == 27):
            coorX = 5
            if segundo == 2:
                coorY = 0
            elif segundo == 7:
                coorY = 2
            elif segundo == 12:
                coorY = 4
            elif segundo == 17:
                coorY = 6
            elif segundo == 22:
                coorY = 8
            elif segundo == 27:
                coorY = 10
        elif(segundo == 3 or segundo == 8 or segundo == 13 or segundo == 18 or segundo == 23 or segundo == 28):
            coorX = 7
            if segundo == 3:
                coorY = 0
            elif segundo == 8:
                coorY = 2
            elif segundo == 13:
                coorY = 4
            elif segundo == 18:
                coorY = 6
            elif segundo == 23:
                coorY = 8
            elif segundo == 28:
                coorY = 10
        elif(segundo == 4 or segundo == 9 or segundo == 14 or segundo == 19 or segundo == 24 or segundo == 29):
            coorX = 9
            if segundo == 4:
                coorY = 0
            elif segundo == 9:
                coorY = 2
            elif segundo == 14:
                coorY = 4
            elif segundo == 19:
                coorY = 6
            elif segundo == 24:
                coorY = 8
            elif segundo == 29:
                coorY = 10
    elif(primero == 1):
        if (segundo == 0 or segundo == 1 or segundo == 2 or segundo == 3 or segundo == 4 or segundo == 5):
            # Coordenada
            coorY = 1
            if segundo == 0:
                coorX = 0
            elif segundo == 1:
                coorX = 2
            elif segundo == 2:
                coorX = 4
            elif segundo == 3:
                coorX = 6
            elif segundo == 4:
                coorX = 8
            elif segundo == 5:
                coorX = 10
        elif (segundo == 6 or segundo == 7 or segundo == 8 or segundo == 9 or segundo == 10 or segundo == 11):
            # Coordenada 3
            coorY = 3
            if segundo == 6:
                coorX = 0
            elif segundo == 7:
                coorX = 2
            elif segundo == 8:
                coorX = 4
            elif segundo == 9:
                coorX = 6
            elif segundo == 10:
                coorX = 8
            elif segundo == 11:
                coorX = 10
        elif (segundo == 12 or segundo == 13 or segundo == 14 or segundo == 15 or segundo == 16 or segundo == 17):
            # coordenada 5
            coorY = 5
            if segundo == 12:
                coorX = 0
            elif segundo == 13:
                coorX = 2
            elif segundo == 14:
                coorX = 4
            elif segundo == 15:
                coorX = 6
            elif segundo == 16:
                coorX = 8
            elif segundo == 17:
                coorX = 10
        elif (segundo == 18 or segundo == 19 or segundo == 20 or segundo == 21 or segundo == 22 or segundo == 23):
            # coordenada 7
            coorY = 7
            if segundo == 18:
                coorX = 0
            elif segundo == 19:
                coorX = 2
            elif segundo == 20:
                coorX = 4
            elif segundo == 21:
                coorX = 6
            elif segundo == 22:
                coorX = 8
            elif segundo == 23:
                coorX = 10
        elif (segundo == 24 or segundo == 25 or segundo == 26 or segundo == 27 or segundo == 28 or segundo == 29):
            # coordenada 9
            coorY = 9
            if segundo == 24:
                coorX = 0
            elif segundo == 25:
                coorX = 2
            elif segundo == 26:
                coorX = 4
            elif segundo == 27:
                coorX = 6
            elif segundo == 28:
                coorX = 8
            elif segundo == 29:
                coorX = 10

    return coorX, coorY

# ? método para convertir de coordenada a tablero


def fromCoordToBoard(CoordX, CoordY):
    primero = -5
    segundo = -5
    if (CoordX == 1 or CoordX == 3 or CoordX == 5 or CoordX == 7 or CoordX == 9):
        primero = 0
    elif(CoordX == 0 or CoordX == 4 or CoordX == 2 or CoordX == 6 or CoordX == 8 or CoordX == 10):
        primero = 1

    # Fila Y=0
    if (CoordX == 1 and CoordY == 0):
        segundo = 0
    elif(CoordX == 3 and CoordY == 0):
        segundo = 1
    elif(CoordX == 5 and CoordY == 0):
        segundo = 2
    elif(CoordX == 7 and CoordY == 0):
        segundo = 3
    elif(CoordX == 9 and CoordY == 0):
        segundo = 4

    # fila Y=2
    if (CoordX == 1 and CoordY == 2):
        segundo = 5
    elif(CoordX == 3 and CoordY == 2):
        segundo = 6
    elif(CoordX == 5 and CoordY == 2):
        segundo = 7
    elif(CoordX == 7 and CoordY == 2):
        segundo = 8
    elif(CoordX == 9 and CoordY == 2):
        segundo = 9

     # fila Y=4
    if (CoordX == 1 and CoordY == 4):
        segundo = 10
    elif(CoordX == 3 and CoordY == 4):
        segundo = 11
    elif(CoordX == 5 and CoordY == 4):
        segundo = 12
    elif(CoordX == 7 and CoordY == 4):
        segundo = 13
    elif(CoordX == 9 and CoordY == 4):
        segundo = 14

    # fila Y=6
    if (CoordX == 1 and CoordY == 6):
        segundo = 15
    elif(CoordX == 3 and CoordY == 6):
        segundo = 16
    elif(CoordX == 5 and CoordY == 6):
        segundo = 17
    elif(CoordX == 7 and CoordY == 6):
        segundo = 18
    elif(CoordX == 9 and CoordY == 6):
        segundo = 19

    # fila Y=8
    if (CoordX == 1 and CoordY == 8):
        segundo = 20
    elif(CoordX == 3 and CoordY == 8):
        segundo = 21
    elif(CoordX == 5 and CoordY == 8):
        segundo = 22
    elif(CoordX == 7 and CoordY == 8):
        segundo = 23
    elif(CoordX == 9 and CoordY == 8):
        segundo = 24

    # fila Y=10
    if (CoordX == 1 and CoordY == 10):
        segundo = 25
    elif(CoordX == 3 and CoordY == 10):
        segundo = 26
    elif(CoordX == 5 and CoordY == 10):
        segundo = 27
    elif(CoordX == 7 and CoordY == 10):
        segundo = 28
    elif(CoordX == 9 and CoordY == 10):
        segundo = 29

     # fila Y=1
    if (CoordX == 0 and CoordY == 1):
        segundo = 0
    elif(CoordX == 2 and CoordY == 1):
        segundo = 1
    elif(CoordX == 4 and CoordY == 1):
        segundo = 2
    elif(CoordX == 6 and CoordY == 1):
        segundo = 3
    elif(CoordX == 8 and CoordY == 1):
        segundo = 4
    elif(CoordX == 10 and CoordY == 1):
        segundo = 5

     # fila Y=3
    if(CoordX == 0 and CoordY == 3):
        segundo = 6
    elif(CoordX == 2 and CoordY == 3):
        segundo = 7
    elif(CoordX == 4 and CoordY == 3):
        segundo = 8
    elif(CoordX == 6 and CoordY == 3):
        segundo = 9
    elif(CoordX == 8 and CoordY == 3):
        segundo = 10
    elif(CoordX == 10 and CoordY == 3):
        segundo = 11

     # fila Y=5
    if(CoordX == 0 and CoordY == 5):
        segundo = 12
    elif(CoordX == 2 and CoordY == 5):
        segundo = 13
    elif(CoordX == 4 and CoordY == 5):
        segundo = 14
    elif(CoordX == 6 and CoordY == 5):
        segundo = 15
    elif(CoordX == 8 and CoordY == 5):
        segundo = 16
    elif(CoordX == 10 and CoordY == 5):
        segundo = 17

     # fila Y=7
    if(CoordX == 0 and CoordY == 7):
        segundo = 18
    elif(CoordX == 2 and CoordY == 7):
        segundo = 19
    elif(CoordX == 4 and CoordY == 7):
        segundo = 20
    elif(CoordX == 6 and CoordY == 7):
        segundo = 21
    elif(CoordX == 8 and CoordY == 7):
        segundo = 22
    elif(CoordX == 10 and CoordY == 7):
        segundo = 23

     # fila Y=9
    if(CoordX == 0 and CoordY == 9):
        segundo = 24
    elif(CoordX == 2 and CoordY == 9):
        segundo = 25
    elif(CoordX == 4 and CoordY == 9):
        segundo = 26
    elif(CoordX == 6 and CoordY == 9):
        segundo = 27
    elif(CoordX == 8 and CoordY == 9):
        segundo = 28
    elif(CoordX == 10 and CoordY == 9):
        segundo = 29

    return primero, segundo

