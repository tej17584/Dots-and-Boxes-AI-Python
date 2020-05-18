# Zona de imports de librerías
import socketio
import numpy as np


# Zona de definir protocolo
sio = socketio.Client()

# clase para la info del juego


class infoGame:
    # Definimos el init
    def __init__(self):
        self.username = ""
        self.tournament_id = ""
        self.game_id = ""
        self.board = []

# Que se connecte
@sio.on('connect')
def onConnect():
    sio.emit('signin', {
        'user_name': infoGame.username,
        'tournament_id': infoGame.tournament_id,
        'user_role': 'player'
    })

#Evento de conexión
@sio.event
def conn_error():
    print("La conexión falló.")


@sio.event
def disconnect():
    print("Desconectado")

#Evento de
@sio.on('ready')
def ready(server):
    typeLine = int(input("0: Horizontal\n 1: Vertical\n"))
    position = int(input("0-29: "))

    while int(infoGame.board[typeLine][position] != 99):
        typeLine = int(input("0: Horizontal\n 1: Vertical\n"))
        position = int(input("0-29: "))

    sio.emit('play', {
        'player_turn_id': server.player_turn_id,
        'tournament_id': infoGame.tournament_id,
        'game_id': infoGame.game_id,
        'movement': (position, typeLine)
    })


def reset():
    row = np.ones(30) * 99
    infoGame.board = [np.ndarray.tolist(row), np.ndarray.tolist(row)]


@sio.on('finish')
def finish(server):
    reset()

    if server['player_turn_id'] == server['winner_turn_id']:
        print("Eres el ganador")
    else:
        print("Perdiste")

    sio.emit('player_ready', {
        'tournament_id': infoGame.tournament_id,
        'game_id': infoGame.game_id,
        'player_turn_id': 0
    })


infoGame = infoGame()
infoGame.username = input("Ingrese el username: \n")
infoGame.tournament_id = input("Ingrese el torneo ID: \n")
host = input("Ingrese el host: ")
sio.connect(host)
