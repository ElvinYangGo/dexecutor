from ChannelHandler import ChannelHandler
from ChannelBuffer import ChannelBuffer
from Channel import Channel

class ClientChannelHandler(ChannelHandler):
	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		channel.write(ChannelBuffer(bytes('Hello World!', 'utf8')))
		self.sentCount = 1

	def messageReceived(self, channel, channelBuffer):
		data = channelBuffer.readAllBytes().decode('utf8')
		print(data)
		if self.sentCount <= 3:
			channel.write(ChannelBuffer(bytes(data, 'utf8')))
			self.sentCount += 1

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
