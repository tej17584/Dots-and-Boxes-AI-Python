
""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: Nodes.py
Propósito: construir los nodos del arbol """

class Nodo:  #clase para nodos
    def __init__(self, currentState):
        self.Current = currentState
        self.CurrentScore = 0
        self.children = {}

    #se genera un childNode para el estado actual
    def Make(self, i, j, player):  
        self.children[(i, j)] = Nodo(self.Current.Get_currentState())
        mul = 1
        if player:
            mul *= -1
        self.children[(i, j)].CurrentScore = (
            self.children[(i, j)].Current.action(i, j) * mul) + self.CurrentScore

    #se agrega un nodo al arbol
    def Populate(self, i, j, Child): 
        self.children[(i, j)] = Child

    #funcion para dibujar la matriz del tablero
    def Draw(self):
        self.Current.Draw_mat()
