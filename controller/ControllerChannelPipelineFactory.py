from common.ChannelPipeline import ChannelPipeline
from controller.ControllerChannelHandler import ControllerChannelHandler 
from common.BufferHeadCodec import BufferHeadCodec

class ControllerChannelPipelineFactory:
	def createChannelPipeline(self):
		channelPipeline = ChannelPipeline()
		channelPipeline.append("ClientChannelHandler", ControllerChannelHandler())
		channelPipeline.append("Codec", BufferHeadCodec())
		return channelPipeline