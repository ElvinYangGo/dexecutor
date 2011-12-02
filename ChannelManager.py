from ChannelBufferFactory import ChannelBufferFactory

class ChannelManager:
	def __init__(self):
		self.channels = []
		
	def addChannel(self, channel):
		self.channels.append(channel)
		
	def removeChannel(self, channel):
		self.channels = [item for item in self.channels if item is not channel]
		
	def sendToAllChannelsExcept(self, channel, data):
		channelBuffer = ChannelBufferFactory.createChannelBuffer(data)
		for item in self.channels:
			if item is not channel:
				item.write(channelBuffer)
		
channelManager = ChannelManager()