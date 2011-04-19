import socket
import select

class Reactor:
	def __init__(self, ip, port):
		self.initServerSock(ip, port)
		self.input = [self.serverSock]

	def initServerSock(self, ip, port):
		self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSock.bind((ip, port))
		self.serverSock.listen(5)

	def serveOnce(self):
		inputReady, outputReady, exceptReady = select.select(self.input, [], [], 0)
		for sock in inputReady:
			if sock == self.serverSock:
				newSock, newAddress = self.serverSock.accept()
				self.input.append(newSock)
				print('new connection: ', newAddress)
			else:
				data = sock.recv(1024)
				if data:
					print(data.decode('utf8'))
					sock.send(data)
				else:
					sock.close()
					self.input.remove(sock)

if '__main__' == __name__:
	reactor = Reactor('localhost', 23567)
	while True:
		reactor.serveOnce()
		import time
		time.sleep(0.5)
