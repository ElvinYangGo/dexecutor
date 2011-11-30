from ChannelHandler import ChannelHandler
from Protocol import Protocol
from ControllerCommandReceivedExecutor import ControllerCommandReceivedExecutor

class ControllerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.CONTROLLER_COMMAND_RECEIVED, ControllerCommandReceivedExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		#self.sendProgramCommand(channel)

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
