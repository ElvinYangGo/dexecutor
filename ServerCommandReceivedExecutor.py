from CommandExecutor import CommandExecutor

class ServerCommandReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		pass
