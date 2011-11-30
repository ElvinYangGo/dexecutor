"""
import ftplib
import pickle
from ChannelBuffer import ChannelBuffer
from CommandExecutor import CommandExecutor
from ChannelBufferFactory import ChannelBufferFactory
import os

class ClientFtpCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('FtpLoginDataNotify', self.onFtpLoginDataNotify)
		self.registerHandler('FtpDirectoryNotify', self.onFtpDirectoryNotify)
		self.messageType = 'Ftp'

	def onFtpLoginDataNotify(self, channel, ftpData):
		self.ftpHandler = ftplib.FTP(ftpData['IP'], ftpData['UserName'], ftpData['Password'])
		command = {'ID':'FtpLoginDataReceived', 'Data':None}
		channel.write(ChannelBufferFactory.createChannelBuffer(self.messageType, command))

	def onFtpDirectoryNotify(self, channel, dirData):
		self.ftpDirectory = dirData['Dir']
		self.createDirectory(self.ftpDirectory)
		fileList = self.ftpHandler.nlst(self.ftpDirectory)
		self.storeFtpFiles(fileList)
		command = {'ID':'FtpDirectoryReceived', 'Data':None}
		channel.write(ChannelBufferFactory.createChannelBuffer(self.messageType, command))

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
"""