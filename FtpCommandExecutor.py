import pickle
from ChannelBuffer import ChannelBuffer

class FtpCommandExecutor:
	def __init__(self):
		self.commandHandlers = {}

	def registerHandler(self, commandName, handler):
		self.commandHandlers[commandName] = handler

	def createMessage(self, command):
		message = {
				'Type':'Ftp',
				'Command':command
				}
		return message 

	def createChannelBuffer(self, command):
		pickleBytes = pickle.dumps(self.createMessage(command))
		return ChannelBuffer(pickleBytes)

