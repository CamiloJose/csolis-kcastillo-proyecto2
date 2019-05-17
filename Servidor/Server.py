import socket
from _thread import *
from Player import Player
import pickle
#colores

red  = (255,0,0)
blue = (0,0,255)
# el ip de la computadora que tiene el servidor 
server = "cambie por el IP de la computadora que vaya a utilizar"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

#datos que se envian de la clase player
players = [Player(0,0,50,50,red), Player(100,100, 50,50, blue)]

#thread que se repite de fondo para manterner conexion entre cliente y servidor
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
