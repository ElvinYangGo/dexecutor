from ChannelBuffer import ChannelBuffer
from ChannelHandler import ChannelHandler
from ChannelPipeline import ChannelPipeline

class Channel:
	def __init__(self, sock, address):
		self.sock = sock
		self.address = address
		self.channelBuffer = ChannelBuffer()
		self.channelPipeline = ChannelPipeline(self, ChannelHandler())
		self.channelPipeline.handleChannelConnected()

	def getAddress(self):
		return self.address

	def getSocket(self):
		return self.sock

	def channelBufferReadableBytes(self):
		return self.channelBuffer.readableBytes()

	def appendBytes(self, data):
		self.channelBuffer.append(data)
	
	def handleReceivedBuffer(self):
		self.channelPipeline.handleReceivedBuffer(self.channelBuffer)
	
	def write(self, channelBuffer):
		self.channelPipeline.handleWrite(channelBuffer, self.sock)

	def handleChannelClosed(self):
		self.channelPipeline.handleChannelClosed()
