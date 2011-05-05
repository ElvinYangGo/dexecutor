import socket
import select
from Bootstrap import Bootstrap

class ClientBootstrap(Bootstrap):
	def __init__(self, ip, port):
		Bootstrap.__init__(self)
		self.connect(ip, port)

	def connect(self, ip, port):
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientSocket.connect((ip, port))
		self.inputSockets.append(clientSocket)
		channel = Channel(clientSocket, (ip,port))
		channelPipeline = self.channelPipelineFactory.createChannelPipeline()
		self.relateChannelWithPipeline(channel, channelPipeline)
		self.channels[clientSocket] = channel

	def serveForever(self):
		while(True):
			inputReady, outputReady, exceptReady = select.select(self.inputSockets, [], [], 0)
			for sock in inputReady:
				self.handleRead(sock)

if '__main__' == __name__:
	clientBootstrap = ClientBootstrap('127.0.0.1', 23567)
	clientBootstrap.setPipelineFactory(ChannelPipelineFactory(ChannelHandler()))
	clientBootstrap.serveForever()
