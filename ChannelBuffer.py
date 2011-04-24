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

	def getAllBytes(self):
		return self.buffer

	def getBytes(self, length):
		return self.buffer[:length]

	def skipBytes(self, length):
		self.buffer = self.buffer[length:]

	"""
	def extractPacket(self):
		if ChannelBuffer.PACKET_HEAD_LENGTH < len(self.buffer):
			if self.getPacketSize() <= len(self.buffer[ChannelBuffer.PACKET_HEAD_LENGTH:]):
				packet = self.buffer[ChannelBuffer.PACKET_HEAD_LENGTH:ChannelBuffer.PACKET_HEAD_LENGTH+self.getPacketSize()]
				self.buffer = self.buffer[ChannelBuffer.PACKET_HEAD_LENGTH+self.getPacketSize():]
				return packet
	
	def getPacketSize(self):
		if ChannelBuffer.PACKET_HEAD_LENGTH <= len(self.buffer):
			packetSize, = struct.unpack('!i', self.buffer[:ChannelBuffer.PACKET_HEAD_LENGTH])
			return packetSize
	"""
