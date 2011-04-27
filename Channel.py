from ChannelBuffer import ChannelBuffer
from BufferHeadDecoder import BufferHeadDecoder
from ChannelHandler import ChannelHandler

class Channel:
	decoder = BufferHeadDecoder()

	def __init__(self, sock, address):
		self.sock = sock
		self.address = address
		self.channelBuffer = ChannelBuffer()
		self.channelHandler = ChannelHandler()

	def getAddress(self):
		return self.address

	def getSocket(self):
		return self.sock

	def channelBufferReadableBytes(self):
		return self.channelBuffer.readableBytes()

	def appendBytes(self, data):
		self.channelBuffer.append(data)
	
	def handleReceivedBuffer(self):
		channelBuffer = Channel.decoder.decode(self.channelBuffer)
		self.channelHandler.messageReceived(self, channelBuffer)
