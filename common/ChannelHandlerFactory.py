import copy

class ChannelHandlerFactory:
	def __init__(self, channelHandler):
		self.channelHandler = channelHandler
		self.executors = {}

	def handlerCount(self):
		return len(self.executors)

	def createChannelHandler(self):
		return self.channelHandler(copy.deepcopy(self.executors))

	def registerExecutor(self, messageType, executor):
		self.executors[messageType] = executor
