from CommandExecutor import CommandExecutor
import ClientData

class ClientConfigNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		ClientData.uniqueID = data
		print('got unique id: ', ClientData.uniqueID)
		
