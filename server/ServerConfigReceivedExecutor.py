from common.CommandExecutor import CommandExecutor

class ServerConfigReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print('client got config')
