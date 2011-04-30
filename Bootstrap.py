import socket
import select
from Channel import Channel

class Bootstrap:
	def __init__(self, ip, port):
		self.RECV_SIZE = 4096
		self.LISTEN_BACKLOG = 5

		self.initServerSock(ip, port)
		self.inputSockets = [self.serverSock]
		self.channels = {}

	def initServerSock(self, ip, port):
		self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSock.bind((ip, port))
		self.serverSock.listen(self.LISTEN_BACKLOG)

	def serveOnce(self):
		inputReady, outputReady, exceptReady = select.select(self.inputSockets, [], [], 0)
		for sock in inputReady:
			if sock == self.serverSock:
				self.handleAccept()
			else:
				self.handleRead(sock)

	def serveForever(self):
		while(True):
			self.serveOnce()

	def handleAccept(self):
		newSock, newAddress = self.serverSock.accept()
		self.inputSockets.append(newSock)
		channel = Channel(newSock, newAddress)
		self.channels[newSock] = channel

	def handleRead(self, sock):
		data = sock.recv(self.RECV_SIZE)
		if data:
			self.channels[sock].appendBytes(data)
			self.channels[sock].handleReceivedBuffer()
		else:
			self.handleClose(sock)

	def handleClose(self, sock):
		self.channels[sock].handleChannelClosed()
		del self.channels[sock]
		self.inputSockets.remove(sock)
		sock.close()


if '__main__' == __name__:
	bootstrap = Bootstrap('localhost', 23567)
	while True:
		bootstrap.serveOnce()
		import time
		time.sleep(0.5)
