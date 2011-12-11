import sys
import socket
import threading
import os

def getInputAndSendToSock(sock):
	while True:
		lineData = sys.stdin.readline()
		sock.sendall(lineData.replace('\n', '').handleDownStream('ascii'))
		'''
		while 0 < len(lineData):
			sentSize = sock.send(lineData.handleDownStream('ascii'))
			lineData = lineData[sentSize:]
		'''


class Stdio:
	def __init__(self):
		self.initServerSock()
		self.initInputSockAndThread()

	def initServerSock(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(('127.0.0.1', 0))
		self.server.listen(5)
		self.port = self.server.getsockname()[1]

	def initInputSockAndThread(self):
		self.initInputSock()
		self.initInputThread()

	def initInputSock(self):
		self.clientSockForInput = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientSockForInput.connect(('127.0.0.1', self.port))
		self.serverSockForInput, addr = self.server.accept()
	
	def initInputThread(self):
		inputThread = threading.Thread(target = getInputAndSendToSock, args=(self.clientSockForInput,))
		inputThread.start()

	def read(self):
		data = self.serverSockForInput.recv(1024)
		return data.handleUpStream('ascii').replace(os.linesep, '')
