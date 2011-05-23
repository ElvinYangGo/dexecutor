import ftplib
import pickle
from ChannelBuffer import ChannelBuffer
from FtpCommandExecutor import FtpCommandExecutor

class ClientFtpCommandExecutor(FtpCommandExecutor):
	def __init__(self):
		FtpCommandExecutor.__init__(self)
		self.registerHandler('FtpLoginDataNotify', self.ftpLoginDataReceived)
		self.registerHandler('FtpFolderNotify', self.ftpFolderDataReceived)

	def handleCommand(self, channel, command):
		commandID = command['ID']
		handler = self.commandHandlers.get(commandID)
		if None != handler:
			handler(channel, command['Data'])

	def ftpLoginDataReceived(self, channel, ftpData):
		self.ftpHandler = ftplib.FTP(ftpData['IP'], ftpData['UserName'], ftpData['Password'])
		fileList = ftpHandler.nlst()
		print(fileList)
		command = {'ID':'FtpLoginDataReceived'}
		channel.write(self.createChannelBuffer(command))

	def ftpFolderDataReceived(self, channel, dirData):
		pass 
