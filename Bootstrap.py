import socket
from Channel import Channel

class Bootstrap:
	def __init__(self):
		self.RECV_SIZE = 4096
		self.channels = {}
		self.inputSockets = []

	def setPipelineFactory(self, channelPipelineFactory):
		self.channelPipelineFactory = channelPipelineFactory

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

