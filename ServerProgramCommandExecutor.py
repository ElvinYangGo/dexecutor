from CommandExecutor import CommandExecutor
from Channel import Channel

class ServerProgramCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.messageType = 'ProgramCommand'

	def sendProgramCommand(self, channel):
		command = {'ID':'ListDirectory', 'Data':'notepad.exe'}
		channel.write(self.createChannelBuffer(self.messageType, command))
