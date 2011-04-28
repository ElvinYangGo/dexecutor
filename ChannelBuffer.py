import struct

class ChannelBuffer:
	def __init__(self, data=None):
		if None != data:
			self.buffer = bytearray(data)
		else:
			self.buffer = bytearray()

	def readableBytes(self):
		return len(self.buffer)

	def append(self, data):
		self.buffer += data

	def readBytes(self, length):
		returnBuffer = self.buffer[:length]
		self.buffer = self.buffer[length:]
		return returnBuffer

	def readAllBytes(self):
		return self.readBytes(len(self.buffer))

	def getBytes(self, length):
		return self.buffer[:length]

	def getAllBytes(self):
		return self.buffer

	def skipBytes(self, length):
		self.buffer = self.buffer[length:]
