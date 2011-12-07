from CommandExecutor import CommandExecutor

class ServerFtpUploadReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):	
		print('client uploaded files')
	