import socket
import select
from Channel import Channel

class Bootstrap:
	def __init__(self):
		self.RECV_SIZE = 4096
		self.channels = {}
		self.inputSockets = []

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

