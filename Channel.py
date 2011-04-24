from ChannelBuffer import ChannelBuffer

class Channel:
	def __init__(self, sock, address):
		self.sock = sock
		self.address = address
		self.channelBuffer = ChannelBuffer()

	def getAddress(self):
		return self.address

	def getSocket(self):
		return self.sock

	def bufferReadableBytes(self):
		return self.channelBuffer.readableBytes()

	def appendBuffer(self, data):
		self.channelBuffer.append(data)
	

