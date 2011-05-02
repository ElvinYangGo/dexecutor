from BufferHeadDecoder import BufferHeadDecoder
from BufferHeadEncoder import BufferHeadEncoder

class ChannelPipeline:
	decoder = BufferHeadDecoder()
	encoder = BufferHeadEncoder()

	def __init__(self, channel, *args):
		self.channel = channel
		self.handlers = args

	def handlerCount(self):
		return len(self.handlers)

	def handleChannelConnected(self):
		self.handlers[-1].channelConnected(self.channel)

	def handleChannelClosed(self):
		self.handlers[-1].channelClosed(self.channel)

	def handleReceivedBuffer(self, channelBuffer):
		preHandledBuffer = ChannelPipeline.decoder.decode(channelBuffer)
		self.handlers[-1].messageReceived(self.channel, preHandledBuffer)
	
	def handleWrite(self, channelBuffer, sock):
		preHandledBuffer = ChannelPipeline.encoder.encode(channelBuffer)
		sock.sendall(preHandledBuffer.readAllBytes())
