import struct
from common.ChannelBuffer import ChannelBuffer

class BufferHeadDecoder:
	PACKET_HEAD_LENGTH = struct.calcsize('!i')

	def decode(self, channelBuffer):
		if BufferHeadDecoder.PACKET_HEAD_LENGTH < channelBuffer.readableBytes():
			packetLength, = struct.unpack('!i', channelBuffer.getBytes(BufferHeadDecoder.PACKET_HEAD_LENGTH))
			if BufferHeadDecoder.PACKET_HEAD_LENGTH + packetLength <= channelBuffer.readableBytes():
				channelBuffer.skipBytes(BufferHeadDecoder.PACKET_HEAD_LENGTH)
				return ChannelBuffer(channelBuffer.readBytes(packetLength))
		return None

