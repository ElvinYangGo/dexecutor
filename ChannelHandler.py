from ChannelBuffer import ChannelBuffer

class ChannelHandler:
	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def messageReceived(self, channel, channelBuffer):
		data = channelBuffer.readAllBytes().decode('utf8')
		print(data)
		channel.write(ChannelBuffer(bytes(data, 'utf8')))
