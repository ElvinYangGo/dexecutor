from common.ChannelPipeline import ChannelPipeline
from server.ServerChannelHandler import ServerChannelHandler
from common.BufferHeadCodec import BufferHeadCodec

class ServerChannelPipelineFactory:
	def __init__(self, channelManager):
		self.channelManager = channelManager

	def createChannelPipeline(self):
		channelPipeline = ChannelPipeline()
		channelPipeline.append("ServerChannelHandler", ServerChannelHandler(self.channelManager))
		channelPipeline.append("Codec", BufferHeadCodec())
		return channelPipeline