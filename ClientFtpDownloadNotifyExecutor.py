from CommandExecutor import CommandExecutor
import ClientData
import os
import ftplib
from Protocol import Protocol
from ChannelBufferFactory import ChannelBufferFactory

class ClientFtpDownloadNotify(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		ClientData.ftp = ftplib.FTP(ClientData.ftpLoginData['IP'], ClientData.ftpLoginData['UserName'], ClientData.ftpLoginData['Password'])
		self.createDirectory(data)
		fileList = ClientData.ftp.nlst(data)
		self.saveFtpFiles(fileList)
		print('download all files')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.FTP_DOWNLOAD_RECEIVED, None))
		
	def createDirectory(self, directoryName):
		print('create directory: ', directoryName)
		if not os.path.exists(directoryName):
			os.mkdir(directoryName)
			
	def saveFtpFiles(self, fileList):
		for fileName in fileList:
			self.saveFtpFile(fileName)
			
	def saveFtpFile(self, fileName):
		print('create file: ', fileName)
		f = open(fileName, 'wb')
		ClientData.ftp.retrbinary('RETR ' + fileName, f.write) 
		f.close()

