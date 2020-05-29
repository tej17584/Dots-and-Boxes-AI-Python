""" Nombre: Alejandro Tejada
Curso: Inteligencia Artificial
Fecha: 28/05/2020
Programa: cliente.py
Propósito: client de la inteligencia artificial"""


# Zona de imports de librerías
import socketio
import numpy as np
from random import *
from conversores import *
from Algoritmos import *
from DotsAndBoxes import *
from Tablero import *
from Nodos import *

# Zona de definir protocolo
sio = socketio.Client()

# clase para la info del juego


class infoGame:
    # Definimos el init
    def __init__(self):
        row = np.ones((30,), dtype=np.int) * 99
        self.username = ""
        self.tournament_id = 0
        self.game_id = ""
        self.board = []
        self.board.append(np.ndarray.tolist(row))
        self.board.append(np.ndarray.tolist(row))
        self.coordenadaX = -5
        self.coordenadaY = -5
        # colocamos un valor de lookahead=2
        self.ValorLookAhead = 2
        # instanciamos el match
        self.Match = DotsAndBoxes(11, 11, self.ValorLookAhead)


# Conversor
def UpdatesLocales(localBoard, serverBoard):

    finalizado = False  # variable para ver si ya terminó la inteligencia
    # colocamos los cambios que hayan de -1.-2,1 o 2 en el otro tablero
    for i in range(len(serverBoard)):
        for j in range(len(serverBoard[i])):
            if (serverBoard[i][j] == 1 or serverBoard[i][j] == -1 or serverBoard[i][j] == -2 or serverBoard[i][j] == 2):
                # ! acá tenemos que actualizar el tablero local
                updateLocalBoard(i, j, serverBoard[i][j])

    # ahora comparamos las diferencias y luego hacemos update del tablero local
    #contador = -1
    localBoardX = localBoard[0]
    localBoardY = localBoard[1]
    serverBoardX = serverBoard[0]
    serverBoardY = serverBoard[1]
    #print(localBoardX)
    #print(localBoardY)
    #print("//////////////////////////////////////////////")
    #print(serverBoardX)
    #print(serverBoardY)

    contador = 0
    # comparamos si hay alguna jugada distinta
    for i in range(len(serverBoard)):
        for j in range(len(serverBoard[i])):
            if (localBoard[i][j] != serverBoard[i][j]):
                infoGame.coordenadaX = i
                infoGame.coordenadaY = j
            if(serverBoard[i][j] == 99):
                contador = contador+1

    # imprpimos lo que el otro player hizo
    #print("COORDENADA JUGADA POR EL OTRO")
    #print(infoGame.coordenadaX)
    #print(infoGame.coordenadaY)
    #print("CONTADOR ", contador)

    # acá aactualizamos el tablero local con la jugada que hizo el otro player
    if infoGame.coordenadaX != -5 and infoGame.coordenadaY != -5:
        updateLocalBoard(infoGame.coordenadaX, infoGame.coordenadaY, 0)

    #print("Coordenada (X,Y)")
    (transformx, transformy) = fromBoardToCoordenate(
        infoGame.coordenadaX, infoGame.coordenadaY)
    #print(transformx, " , ", transformy)

    #!Acá debemos hacer el cambio
    # coordenada de AI
    coordeXAi = -5
    coordeYAi = -5
    primero = -5
    segundo = -5
    if(contador>2):
        if (transformx >= 0 and transformx <= 10) and (transformy >= 0 and transformy <= 10):
            (coordeXAi, coordeYAi) = infoGame.Match.Human(transformx, transformy)

        if (coordeXAi != -5 and coordeYAi != -5):
            #print("Coordenada de AI sugerida")
            (primero, segundo) = fromCoordToBoard(
                coordeXAi, coordeYAi)
            #print(primero, " , ", segundo)

            return primero, segundo
    elif(contador<=2):
         if (transformx >= 0 and transformx <= 10) and (transformy >= 0 and transformy <= 10):
            print("Coordenada variante")
            #(primero, segundo) = fromCoordToBoard(
            #    random, transformy)
            primero=randint(0, 1)
            segundo=randint(0,29)
            #print(primero, " , ", segundo)

            return primero, segundo

# ? método para convetir el bord


def updateLocalBoard(Primero, Segundo, valor):
    #print("Update tablero local")
    infoGame.board[Primero][Segundo] = valor


# Que se connecte
@sio.on('connect')
def onConnect():
    sio.emit('signin', {
        'user_name': infoGame.username,
        'tournament_id': infoGame.tournament_id,
        'user_role': 'player'
    })

# Evento de conexión
@sio.event
def conn_error():
    print("La conexión falló.")


@sio.event
def disconnect():
    print("Desconectado")

# Evento de
@sio.on('ready')
def ready(server):
    finalizadoMain = False
    print("------------------------------------------------------")
    # print(infoGame.board)

    if infoGame.coordenadaX == -5 and infoGame.coordenadaY == -5:
        UpdatesLocales(infoGame.board, server["board"])
        (nuevaCoorx, nuevaCoordY) = infoGame.Match.Computer()
        (coordX, coordY) = fromCoordToBoard(nuevaCoorx, nuevaCoordY)
        #print("Las coordenadas para la primer tirada son")
        #print(coordX)
        #print(coordY)
        #tipoPlayer = input("Ingresa 0 o 1: \n")
        #position = input("Ingresa 0 a 29: \n")
        #!random de la posicion
        #tipoPlayer = randint(0, 1)
        #! random del lugar
        #position = randint(0, 29)
        print("Voy a emitir POR PRIMERA VEZ")
        sio.emit('play', {
            'player_turn_id': server['player_turn_id'],
            'tournament_id': infoGame.tournament_id,
            'game_id': server['game_id'],
            'movement': [coordX, coordY]
        })

        updateLocalBoard(int(coordX), int(coordY), 0)
    else:
        #tipoPlayer = input("Ingresa 0 o 1: \n")
        #position = input("Ingresa 0 a 29: \n")
        (FirtsCoord, SecondCoord) = UpdatesLocales(
            infoGame.board, server["board"])
        #print("Las coordenadas para la primer tirada son")
        # print(coordX)
        # print(coordY)
        #tipoPlayer = input("Ingresa 0 o 1: \n")
        #position = input("Ingresa 0 a 29: \n")
        #!random de la posicion
        #tipoPlayer = randint(0, 1)
        #! random del lugar
        #position = randint(0, 29)
        if FirtsCoord != -5 and SecondCoord != -5 and finalizadoMain != True:
            print("Voy a emitir NORMAL")
            sio.emit('play', {
                'player_turn_id': server['player_turn_id'],
                'tournament_id': infoGame.tournament_id,
                'game_id': server['game_id'],
                'movement': [FirtsCoord, SecondCoord]
            })

            updateLocalBoard(int(FirtsCoord), int(SecondCoord), 0)
        else:
            print("Voy a emitir VARIANTE2")
            sio.emit('play', {
                'player_turn_id': server['player_turn_id'],
                'tournament_id': infoGame.tournament_id,
                'game_id': server['game_id'],
                'movement': [FirtsCoord, SecondCoord]
            })

            updateLocalBoard(int(FirtsCoord), int(SecondCoord), 0)


def reset():
    row = np.ones((30,), dtype=np.int) * 99
    #infoGame.board = [np.ndarray.tolist(row), np.ndarray.tolist(row)]
    infoGame.board=[]
    infoGame.board.append(np.ndarray.tolist(row))
    infoGame.board.append(np.ndarray.tolist(row))
    infoGame.coordenadaX=-5
    infoGame.coordenadaY=-5
    infoGame.ValorLookAhead=2
    infoGame.Match=DotsAndBoxes(11,11,infoGame.ValorLookAhead)



@sio.on('finish')
def finish(server):
    reset()

    if server['player_turn_id'] == server['winner_turn_id']:
        print("Eres el ganador")
    else:
        print("Perdiste")

    sio.emit('player_ready', {
        'tournament_id': infoGame.tournament_id,
        'game_id': server['game_id'],
        'player_turn_id': server['player_turn_id']
    })


infoGame = infoGame()
infoGame.username = input("Ingrese el username: \n")
infoGame.tournament_id = int(input("Ingrese el torneo ID: \n"))
host = "http://localhost:"+input("Ingrese el host: ")
sio.connect(host)
