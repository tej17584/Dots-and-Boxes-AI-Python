""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: Board.py
Propósito: dibujar el tablero y su lógica """

#zona de librerías
#------------------------
from random import *
#--------------------------
#la clase game se encarga de manejar loq ue sucede en el tablero
class Tablero:  
    def __init__(self, Mat, dimX, dimY):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY

    #se instancia el tablero con las dimensiones
    def Initiate(self):  
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    #! se llena de valores random lo de adentro
                    R.append(randint(1, 9))
                elif i % 2 == 0 and j % 2 == 0:
                    #mprimiendo los asteriscos
                    R.append('*')
                else:
                    R.append(' ')  # se agregan espacio
            self.Mat.append(R)

    def Get_matrix(self):  # Matriz se obtiene
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    # se duibuja el tablero
    def Draw_mat(self):  

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX):
            print(str(i), end='  ')
        print()

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX + 1):
            print("___", end='')
        print()
        for j in range(self.dimY):
            if self.dimX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimX):
                print(str(self.Mat[j][z]), end='  ')
            print()
        print("   _________________________\n")

    def Get_currentState(self):
        return Tablero(self.Get_matrix(), self.dimX, self.dimY)

    #se aplican las acciones al tablero
    def action(self, i, j):  
        Sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        else:
            self.Mat[j][i] = '|'
            if i < self.dimX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]
        return Sum
