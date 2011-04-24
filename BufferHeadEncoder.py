import struct

class BufferHeadEncoder:
	def encode(self, buffer):
		return struct.pack('!i' + str(len(buffer)) + 's', len(buffer), buffer)

