import struct

class ChannelBuffer:
	PACKET_HEAD_LENGTH = 4
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
