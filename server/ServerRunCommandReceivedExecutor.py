from common.CommandExecutor import CommandExecutor

class ServerRunCommandReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		pass
