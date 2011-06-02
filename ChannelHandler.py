from ChannelBuffer import ChannelBuffer
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
		messageType = message['Type']
		self.executors[messageType].handleCommand(channel, message['Command'])

	def channelClosed(self, channel):
		pass
#		print(channel.getAddress(), ' closed')

	def registerExecutor(self, messageType, executor):
		self.executors[messageType] = executor
