from common.ChannelHandler import ChannelHandler
from common.Protocol import Protocol
from controller.ControllerCommandReceivedExecutor import ControllerCommandReceivedExecutor

class ControllerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.CONTROLLER_COMMAND_RECEIVED, ControllerCommandReceivedExecutor())

	def handleConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def handleDisconnected(self, channel):
		print(channel.getAddress(), ' closed')
