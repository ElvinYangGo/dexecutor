
class ChannelPipeline:
	def __init__(self):
		self.handlers = []
		
	def append(self, name, handler):
		self.handlers.append((name, handler))
	
	def remove(self, name):
		self.handlers = [entry for entry in self.handlers if entry[0] != name]
	
	def setChannel(self, channel):
		self.channel = channel

	def handlerCount(self):
		return len(self.handlers)

	def handleConnected(self):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handleConnected'):
				entry[1].handleConnected(self.channel)
			
	def handleDisconnected(self):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handleDisconnected'):
				entry[1].handleDisconnected(self.channel)

	def handleUpStream(self, channelBuffer):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handleUpStream'):
				channelBuffer = entry[1].handleUpStream(self.channel, channelBuffer)
				if channelBuffer == None:
					break

	def handleDownStream(self, channelBuffer, sock):
		for entry in self.handlers:
			if hasattr(entry[1], 'handleDownStream'):
				channelBuffer = entry[1].handleDownStream(self.channel, channelBuffer)
				if channelBuffer == None:
					break
		sock.sendall(channelBuffer.readAllBytes())
