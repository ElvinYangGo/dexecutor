from common.CommandExecutor import CommandExecutor

class ServerStopCommandReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print('client got stop command')
