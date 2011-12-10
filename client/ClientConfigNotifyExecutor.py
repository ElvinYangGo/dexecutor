from common.CommandExecutor import CommandExecutor
import client.ClientData

class ClientConfigNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		client.ClientData.uniqueID = data
		print('got unique id: ', client.ClientData.uniqueID)
		
