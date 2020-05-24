# Zona de imports de librerías
import socketio
import numpy as np
from random import *

# Zona de definir protocolo
sio = socketio.Client()

# clase para la info del juego


class infoGame:
    # Definimos el init
    def __init__(self):
        self.username = ""
        self.tournament_id = 0
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
    #!random de la posicion
    tipoPlayer = randint(0, 1)
    #! random del lugar
    position = randint(0, 29)
    print("Voy a emitir")
    sio.emit('play', {
        'player_turn_id': server['player_turn_id'],
        'tournament_id': infoGame.tournament_id,
        'game_id': server['game_id'],
        'movement': [tipoPlayer, position]
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
        'game_id': server['game_id'],
        'player_turn_id': server['player_turn_id']
    })


infoGame = infoGame()
infoGame.username = input("Ingrese el username: \n")
infoGame.tournament_id = int(input("Ingrese el torneo ID: \n"))
host = "http://localhost:"+input("Ingrese el host: ")
sio.connect(host)
