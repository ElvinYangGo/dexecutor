import socket
import select
from Channel import Channel

class Reactor:
	def __init__(self, ip, port):
		self.BUFFER_ENCODE = 'utf8'
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

	def handleAccept(self):
		newSock, newAddress = self.serverSock.accept()
		self.inputSockets.append(newSock)
		print('new connection: ', newAddress)
		channel = Channel(newSock, newAddress)
		self.channels[newSock] = channel

	def handleRead(self, sock):
		data = sock.recv(self.RECV_SIZE)
		if data:
			print(data.decode(self.BUFFER_ENCODE))
			sock.send(data)
			self.channels[sock].appendBuffer(data)
		else:
			sock.close()
			self.inputSockets.remove(sock)

if '__main__' == __name__:
	reactor = Reactor('localhost', 23567)
	while True:
		reactor.serveOnce()
		import time
		time.sleep(0.5)
