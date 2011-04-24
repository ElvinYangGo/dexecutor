import struct
from ChannelBuffer import ChannelBuffer

class BufferHeadEncoder:
	def encode(self, channelBuffer):
		buffer = channelBuffer.getAllBytes()
		encodedBytes = struct.pack('!i' + str(len(buffer)) + 's', len(buffer), buffer)
		return ChannelBuffer(encodedBytes)

