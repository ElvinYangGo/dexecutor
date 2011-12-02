from CommandExecutor import CommandExecutor
from ChannelManager import channelManager
from Protocol import Protocol

class ServerControllerCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		index = data.find(' ')
		controllerCommand = data[:index]
		controllerData = data[index+1:]
		print(data, controllerCommand, controllerData)
		dataToSend = {'ID':Protocol.COMMAND_NOTIFY, 'Data':controllerData}
		channelManager.sendToAllChannelsExcept(channel, dataToSend)
		
