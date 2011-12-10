import copy
from common.ChannelPipeline import ChannelPipeline

class ChannelPipelineFactory:
	def __init__(self, *args):
		self.handlers = args

	def handlerCount(self):
		return len(self.handlers)

	def createChannelPipeline(self):
		return ChannelPipeline(copy.deepcopy(self.handlers))
