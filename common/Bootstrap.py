import socket

class Bootstrap:
	def __init__(self, channelManager):
		self.channelManager = channelManager
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
				self.channels[sock].appendBytes(data)
				self.channels[sock].handleUpStream()
			else:
				self.handleClose(sock)

	def handleClose(self, sock):
		self.channels[sock].handleDisconnected()
		self.channelManager.removeChannel(self.channels[sock])
		del self.channels[sock]
		self.inputSockets.remove(sock)
		sock.close()

