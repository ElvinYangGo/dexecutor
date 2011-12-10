from common.CommandExecutor import CommandExecutor

class ServerFtpDownloadReceivedExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):	
		print('client downloaded files')
	

