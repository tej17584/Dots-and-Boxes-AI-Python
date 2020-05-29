""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: DostnBoxes.py
Propósito: lógica del tablero"""


#Zona de librerias
#------------------------------
from random import *
import collections
from Algoritmos import *
from Tablero import *
from Nodos import *
#--------------------------

class DotsAndBoxes:  # Clase para los valores de humano y de computadora
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num):
        #! estado actual del game del board
        currentState = Tablero([], Board_Xdim, Board_Ydim)  # Tablero.py
        currentState.Initiate()  # Tablero.py
        self.State = Nodo(currentState)  # Nodos.py
        # numero de jugadores
        self.Ply_num = Ply_num
        self.Score = 0

    # Acciones del jugador
    def Human(self, CoordenadaNuevaX, CoordenadaNuevaY):
        finishHuman=False
        jugadaAIx = -5
        jugadaAIy = -5
        # HumanX = int(
        #    input("Please enter the 'X' coordinate of your choice (an integer such as 4): "))
        # HumanY = int(
        #    input("Please enter the 'Y' coordinate of your choice (an integer such as 4): "))
        #print("ENTRE ACA")
        if (CoordenadaNuevaX, CoordenadaNuevaY) not in self.State.children:
            self.State.Make(CoordenadaNuevaX, CoordenadaNuevaY, False)
            self.State = self.State.children[(
                CoordenadaNuevaX, CoordenadaNuevaY)]
        else:
            self.State = self.State.children[(
                CoordenadaNuevaX, CoordenadaNuevaY)]

        #print("Current Score =====>> Your Score - AI Score = " +
        #      str(self.State.CurrentScore), end="\n\n\n")

        #self.State.Draw()
        (jugadaAIx, jugadaAIy) = self.Computer()
        if (jugadaAIx != -5 and jugadaAIy != -5):
            return jugadaAIx, jugadaAIy

    #acciones de computadora de la inteligencia
    def Computer(self): 
      
        finishComputer=False
        move = Algoritmos.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        # print("AI selected the following coordinates to play:\n" +
        #      "(", str(move[0]), ", " + str(move[1]), ")", end="\n\n")

        # print("Current Score =====>> Your Score - AI Score = " +
        #      str(self.State.CurrentScore), end="\n\n\n")
        #self.State.Draw()
        #if len(self.State.children) == 0:
        #    self.State.Draw()
        #    self.Evaluation()
        #    finishComputer=True
        #    return
        #else:
        return int(move[0]), int(move[1])

        # self.Human()

    """ def Evaluation(self):  # Evaluation function for taking care of the final scores
        print("Stop this Madness!!!\n")
        if self.State.CurrentScore > 0:
            print(
                "You won you crazy little unicorn!! You are the new hope for the mankind!")
            #return
            exit()
            return
        elif self.State.CurrentScore < 0:
            print("!!! Inevitable Doom!!! You were crushed by the AI!! ")
            exit()
            return
        else:
            print("Draw! Well Congratulations! you are as smart as the AI!")
            exit()
            return """

    def start(self):
        self.Human()
    
   
