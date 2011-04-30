import socket
import select
from Bootstrap import Bootstrap
from Channel import Channel

class ServerBootstrap(Bootstrap):
	def __init__(self, ip, port):
		Bootstrap.__init__(self)
		self.bindServer(ip, port)

	def bindServer(self, ip, port):
		self.LISTEN_BACKLOG = 5
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.bind((ip, port))
		self.serverSocket.listen(self.LISTEN_BACKLOG)
		self.inputSockets.append(self.serverSocket)

	def serveOnce(self):
		inputReady, outputReady, exceptReady = select.select(self.inputSockets, [], [], 0)
		for sock in inputReady:
			if sock == self.serverSocket:
				self.handleAccept()
			else:
				self.handleRead(sock)

	def handleAccept(self):
		newSock, newAddress = self.serverSocket.accept()
		self.inputSockets.append(newSock)
		channel = Channel(newSock, newAddress)
		self.channels[newSock] = channel

if '__main__' == __name__:
	serverBootstrap = ServerBootstrap('localhost', 23567)
	while True:
		serverBootstrap.serveOnce()
		import time
		time.sleep(0.5)
