import socket
from ChannelManager import ChannelManager
from ChannelManager import channelManager

class Bootstrap:
	def __init__(self):
		self.RECV_SIZE = 4096
		self.channels = {}
		self.inputSockets = []

	def setPipelineFactory(self, channelPipelineFactory):
		self.channelPipelineFactory = channelPipelineFactory

	def relateChannelWithPipeline(self, channel, channelPipeline):
		channelPipeline.setChannel(channel)
		channel.setChannelPipeline(channelPipeline)

	def handleRead(self, sock):
		try:
			data = sock.recv(self.RECV_SIZE)
		except socket.error as errorInstance:
			print('errno: ', errorInstance.errno, ', ', errorInstance.strerror)
			self.handleClose(sock)
		else:
			if data:
				print('recv: ', len(data))
				self.channels[sock].appendBytes(data)
				self.channels[sock].handleReceivedBuffer()
			else:
				self.handleClose(sock)

	def handleClose(self, sock):
		self.channels[sock].handleChannelClosed()
		channelManager.removeChannel(self.channels[sock])
		del self.channels[sock]
		self.inputSockets.remove(sock)
		sock.close()

