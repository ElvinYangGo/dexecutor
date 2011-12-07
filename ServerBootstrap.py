import socket
import select
import time
from Bootstrap import Bootstrap
from Channel import Channel
from ChannelPipelineFactory import ChannelPipelineFactory
from ServerChannelHandler import ServerChannelHandler
from ChannelManager import ChannelManager
from ChannelManager import channelManager

class ServerBootstrap(Bootstrap):
	def __init__(self):
		Bootstrap.__init__(self)

	def bindServer(self, ip, port):
		self.LISTEN_BACKLOG = 5
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
		newSock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		self.inputSockets.append(newSock)
		channel = Channel(newSock, newAddress, channelManager.generatorID())
		channelPipeline = self.channelPipelineFactory.createChannelPipeline()
		self.relateChannelWithPipeline(channel, channelPipeline)
		self.channels[newSock] = channel
		channelManager.addChannel(channel)
		channel.handleConnected()

if '__main__' == __name__:
	serverBootstrap = ServerBootstrap()
	serverBootstrap.setPipelineFactory(ChannelPipelineFactory(ServerChannelHandler()))
	serverBootstrap.bindServer('localhost', 23567)
	while True:
		serverBootstrap.serveOnce()

		try:
			time.sleep(0.5)
		except KeyboardInterrupt:
			print('interrupt')
			break
	print('shutdown')
