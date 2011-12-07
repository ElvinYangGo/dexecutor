from ChannelBufferFactory import ChannelBufferFactory

class ChannelManager:
	def __init__(self):
		self.channels = []
		self.id = 0
		
	def addChannel(self, channel):
		self.channels.append(channel)
		
	def removeChannel(self, channel):
		self.channels = [item for item in self.channels if item is not channel]
		
	def sendToAllChannelsExcept(self, channel, commandID, commandData):
		channelBuffer = ChannelBufferFactory.createChannelBuffer(commandID, commandData)
		for item in self.channels:
			if item is not channel:
				item.write(channelBuffer)
				
	def generatorID(self):
		self.id += 1
		return self.id
				
channelManager = ChannelManager()