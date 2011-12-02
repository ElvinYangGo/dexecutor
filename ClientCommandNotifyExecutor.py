from CommandExecutor import CommandExecutor

class ClientCommandNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print(data)
