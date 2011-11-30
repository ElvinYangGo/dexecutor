import pickle

class ChannelHandler:
	def __init__(self):
		self.executors = {}

	def channelConnected(self, channel):
		pass
#		print(channel.getAddress(), ' connected')

	def messageReceived(self, channel, channelBuffer):
		message = pickle.loads(channelBuffer.readAllBytes())
		print(message)
		messageID = message['ID']
		self.executors[messageID].handleCommand(channel, message['Data'])
		executor = self.executors.get(messageID)
		if executor != None:
			executor.onMessage(channel, message['Data'])		
	
	def channelClosed(self, channel):
		pass
#		print(channel.getAddress(), ' closed')

	def registerExecutor(self, messageID, executor):
		self.executors[messageID] = executor
