from common.ChannelPipeline import ChannelPipeline
from client.ClientChannelHandler import ClientChannelHandler
from common.BufferHeadCodec import BufferHeadCodec

class ClientChannelPipelineFactory:
	def createChannelPipeline(self):
		channelPipeline = ChannelPipeline()
		channelPipeline.append("ClientChannelHandler", ClientChannelHandler())
		channelPipeline.append("Codec", BufferHeadCodec())
		return channelPipeline