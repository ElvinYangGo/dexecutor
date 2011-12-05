from CommandExecutor import CommandExecutor
from ChannelManager import channelManager
from Protocol import Protocol
from ChannelBufferFactory import ChannelBufferFactory

class ServerControllerCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.dispatcher = {}
		self.dispatcher['send_ftp_data'] = self.onFtpLoginData
		self.dispatcher['download'] = self.onDownload
		self.dispatcher['run'] = self.onRun
		
	def onMessage(self, channel, data):
		index = data.find(' ')
		if index == -1:
			controllerCommand = data
			controllerData = ''
		else:
			controllerCommand = data[:index]
			controllerData = data[index+1:]
		handler = self.dispatcher.get(controllerCommand)
		if handler: 
			handler(channel, controllerData)
		
		"""
		controller have to read input in block mode, 
			it can not handle socket's receive data immediately
		controllerCommandReceivedData = {'ID':Protocol.CONTROLLER_COMMAND_RECEIVED, 'Data':''}
		channel.write(ChannelBufferFactory.createChannelBuffer(controllerCommandReceivedData))
		"""
		
		"""
		ToDo:
		handle each command: ftp login data, download, run, stop
		"""

	def onFtpLoginData(self, channel, controllerData):
		ftpData = {
				'IP':'127.0.0.1', 
				'Port':21,
				'UserName':'test',
				'Password':'test'
				}
		channelManager.sendToAllChannelsExcept(channel, Protocol.FTP_LOGIN_DATA_NOTIFY, ftpData)

	def onDownload(self, channel, controllerData):
		channelManager.sendToAllChannelsExcept(channel, Protocol.FTP_DOWNLOADING_NOTIFY, controllerData)

	def onRun(self, channel, controllerData):
		channelManager.sendToAllChannelsExcept(channel, Protocol.COMMAND_NOTIFY, controllerData)