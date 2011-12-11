import pickle

class ChannelHandler:
	def __init__(self):
		self.executors = {}

	def handleConnected(self, channel):
		pass

	def handleUpStream(self, channel, channelBuffer):
		message = pickle.loads(channelBuffer.readAllBytes())
		print(message)
		messageID = message['ID']
		executor = self.executors.get(messageID)
		if executor != None:
			executor.onMessage(channel, message['Data'])		
	
	def handleDisconnected(self, channel):
		pass

	def registerExecutor(self, messageID, executor):
		self.executors[messageID] = executor
