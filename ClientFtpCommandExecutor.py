import ftplib
import pickle
from ChannelBuffer import ChannelBuffer
from CommandExecutor import CommandExecutor
import os

class ClientFtpCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('FtpLoginDataNotify', self.ftpLoginDataReceived)
		self.registerHandler('FtpDirectoryNotify', self.ftpDirectoryDataReceived)

	def ftpLoginDataReceived(self, channel, ftpData):
		self.ftpHandler = ftplib.FTP(ftpData['IP'], ftpData['UserName'], ftpData['Password'])
		command = {'ID':'FtpLoginDataReceived', 'Data':None}
		channel.write(self.createChannelBuffer('Ftp', command))

	def ftpDirectoryDataReceived(self, channel, dirData):
		self.ftpDirectory = dirData['Dir']
		self.createDirectory(self.ftpDirectory)
		fileList = self.ftpHandler.nlst(self.ftpDirectory)
		self.storeFtpFiles(fileList)

	def createDirectory(self, directoryName):
		if not os.path.exists(directoryName):
			os.mkdir(directoryName)
	
	def storeFtpFiles(self, fileList):
		for fileName in fileList:
			self.storeFtpFile(fileName)

	def storeFtpFile(self, fileName):
		f = open(fileName, 'wb')
		self.ftpHandler.retrbinary('RETR ' + fileName, f.write) 
		f.close()
