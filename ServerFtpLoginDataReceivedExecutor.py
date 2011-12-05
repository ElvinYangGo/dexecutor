from CommandExecutor import CommandExecutor

class ServerFtpLoginDataReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)

	def onMessage(self, channel, data):
		print('client got ftp login data')
	
	