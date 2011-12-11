import struct
from common.ChannelBuffer import ChannelBuffer

class BufferHeadCodec:
	PACKET_HEAD_LENGTH = struct.calcsize('!i')

	def handleUpStream(self, channel, channelBuffer):
		if BufferHeadCodec.PACKET_HEAD_LENGTH < channelBuffer.readableBytes():
			packetLength, = struct.unpack('!i', channelBuffer.getBytes(BufferHeadCodec.PACKET_HEAD_LENGTH))
			if BufferHeadCodec.PACKET_HEAD_LENGTH + packetLength <= channelBuffer.readableBytes():
				channelBuffer.skipBytes(BufferHeadCodec.PACKET_HEAD_LENGTH)
				return ChannelBuffer(channelBuffer.readBytes(packetLength))
		return None

	def handleDownStream(self, channel, channelBuffer):
		buffer = channelBuffer.getAllBytes()
		encodedBytes = struct.pack('!i' + str(len(buffer)) + 's', len(buffer), buffer)
		return ChannelBuffer(encodedBytes)

