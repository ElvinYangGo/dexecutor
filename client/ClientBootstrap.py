import socket
import select
from common.Bootstrap import Bootstrap
from common.Channel import Channel
from common.ChannelManager import ChannelManager

class ClientBootstrap(Bootstrap):
	def __init__(self):
		Bootstrap.__init__(self, ChannelManager())

	def connect(self, ip, port):
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		clientSocket.connect((ip, port))
		self.inputSockets.append(clientSocket)
		channel = Channel(clientSocket, (ip,port))
		channelPipeline = self.channelPipelineFactory.createChannelPipeline()
		self.relateChannelWithPipeline(channel, channelPipeline)
		self.channels[clientSocket] = channel
		channel.handleConnected()
		return channel

	def serveOnce(self):
		if self.inputSockets:
			inputReady, outputReady, exceptReady = select.select(self.inputSockets, [], [], 0)
			for sock in inputReady:
				self.handleRead(sock)
