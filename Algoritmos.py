""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: Algoritmos.py
Propósito: algoritmos de alfa beta etc"""

class Algoritmos:

    #! Algoritmo minimax
    def miniMax(State, Ply_num):  

        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
                    if Ply_num < 2:
                        return (i, j)
        #Valor mínmino de heurística
        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algoritmos.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
                i = k[0]
                j = k[1]

        return (i, j)
    # PARTE DEL ALFABETA

    #! MAximum
    # aca pasamos el estado y el alpha
    def Maximum(State, Ply_num, Alpha):
        if Ply_num == 0:
            return State.CurrentScore

        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, False)
        #valor de heurísticac de beta, algunos toman -infinito
        Maximum_Score = -1000
        i = 0
        j = 0
        #valor de alfa beta
        for k, z in State.children.items():
            Result = Algoritmos.Minimum(z, Ply_num - 1, Maximum_Score)
            if Maximum_Score < Result:
                Maximum_Score = Result
            if Result > Alpha:
                return Result

        return Maximum_Score

    #Alfa beta minimum
    def Minimum(State, Ply_num, Beta): 
        if Ply_num == 0:
            return State.CurrentScore
        #estado de los árboles
        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
        #score
        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algoritmos.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
            if Result < Beta:
                return Result

        return Minimum_Score
