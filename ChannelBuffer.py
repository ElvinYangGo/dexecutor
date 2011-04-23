class ChannelBuffer:
	def __init__(self):
		self.buffer = bytearray()

	def readableBytes(self):
		return len(self.buffer)

	def append(self, data):
		self.buffer += data

	def readBytes(self, size):
		returnBuffer = self.buffer[:size]
		self.buffer = self.buffer[size:]
		return returnBuffer

