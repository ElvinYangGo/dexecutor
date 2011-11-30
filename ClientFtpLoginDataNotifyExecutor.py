from CommandExecutor import CommandExecutor

class ClientFtpLoginDataNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		pass