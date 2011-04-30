import socket
from Bootstrap import Bootstrap
from Channel import Channel

class ServerBootstrap(Bootstrap):
	def __init__(self, ip, port):
		Bootstrap.__init__(self)
		self.bindServer(ip, port)

	def bindServer(self, ip, port):
		self.LISTEN_BACKLOG = 5
		self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSock.bind((ip, port))
		self.serverSock.listen(self.LISTEN_BACKLOG)
		self.inputSockets = [self.serverSock]

	def handleAccept(self):
		newSock, newAddress = self.serverSock.accept()
		self.inputSockets.append(newSock)
		channel = Channel(newSock, newAddress)
		self.channels[newSock] = channel

if '__main__' == __name__:
	serverBootstrap = ServerBootstrap('localhost', 23567)
	while True:
		serverBootstrap.serveOnce()
		import time
		time.sleep(0.5)
