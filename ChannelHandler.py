class ChannelHandler:
	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def messageReceived(self, channel, channelBuffer):
		print(channelBuffer.getAllBytes().decode('utf8'))
