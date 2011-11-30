from CommandExecutor import CommandExecutor
from ChannelBufferFactory import ChannelBufferFactory

class ServerProgramCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)

	def sendProgramCommand(self, channel):
		command = {'ID':'ProgramCommandNotify', 'Data':'dir'}
		channel.write(ChannelBufferFactory.createChannelBuffer(self.messageType, command))
