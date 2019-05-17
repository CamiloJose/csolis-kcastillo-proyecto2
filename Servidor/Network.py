import socket
import pickle

#clase que permite la conexion entre cliente y servidor
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # el ip depende de la maquina que tenga el servidor
        self.server = "cambie por el IP de la computadora que vaya a utilizar"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
    #obtener la posicion de los jugadores para el servidor desde el cliente
    def getP(self):
        return self.p
    #conexion entre cliente y servidor
    def connect(self):
        try:
            self.client.connect(self.addr)
                                                #cantidad de bytes que se envian
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    #informacion enviada al cliente desde el servidor
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
