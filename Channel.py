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

	def setChannelPipeline(self, channelPipeline):
		self.channelPipeline = channelPipeline

	def channelBufferReadableBytes(self):
		return self.channelBuffer.readableBytes()

	def appendBytes(self, data):
		self.channelBuffer.append(data)
	
	def handleConnected(self):
		self.channelPipeline.handleChannelConnected()
	
	def handleReceivedBuffer(self):
		self.channelPipeline.handleReceivedBuffer(self.channelBuffer)
	
	def write(self, channelBuffer):
		self.channelPipeline.handleWrite(channelBuffer, self.sock)

	def handleChannelClosed(self):
		self.channelPipeline.handleChannelClosed()
