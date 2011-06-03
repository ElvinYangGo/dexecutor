import pickle
from ChannelBuffer import ChannelBuffer

class CommandExecutor:
	def __init__(self):
		self.commandHandlers = {}

	def registerHandler(self, commandName, handler):
		self.commandHandlers[commandName] = handler

	def createMessage(self, messageType, command):
		message = {
				'Type':messageType,
				'Command':command
				}
		return message 

	def createChannelBuffer(self, messageType, command):
		pickleBytes = pickle.dumps(self.createMessage(messageType, command))
		return ChannelBuffer(pickleBytes)

	def handleCommand(self, channel, command):
		commandID = command['ID']
		handler = self.commandHandlers.get(commandID)
		if None != handler:
			handler(channel, command['Data'])

