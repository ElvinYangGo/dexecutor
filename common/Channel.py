from common.ChannelBuffer import ChannelBuffer

class Channel:
	def __init__(self, sock, address, uniqueID=1):
		self.sock = sock
		self.address = address
		self.uniqueID = uniqueID
		self.channelBuffer = ChannelBuffer()

	def getID(self):
		return self.uniqueID
		
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
		self.channelPipeline.handleConnected()
	
	def handleUpStream(self):
		self.channelPipeline.handleUpStream(self.channelBuffer)
	
	def write(self, channelBuffer):
		self.channelPipeline.handleDownStream(channelBuffer, self.sock)

	def handleDisconnected(self):
		self.channelPipeline.handleDisconnected()
