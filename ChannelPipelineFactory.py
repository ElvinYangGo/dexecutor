class ChannelPipelineFactory:
	def __init__(self, *args):
		self.handlers = args

	def handlerCount(self):
		return len(self.handlers)
