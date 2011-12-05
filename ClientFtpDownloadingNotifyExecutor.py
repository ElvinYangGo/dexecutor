from CommandExecutor import CommandExecutor
import ClientData
import os
import ftplib
from Protocol import Protocol
from ChannelBufferFactory import ChannelBufferFactory

class ClientFtpDownloadingNotify(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		#print(data)
		ClientData.ftp = ftplib.FTP(ClientData.ftpLoginData['IP'], ClientData.ftpLoginData['UserName'], ClientData.ftpLoginData['Password'])
		print('create ftp instance')
		self.createDirectory(data)
		fileList = ClientData.ftp.nlst(data)
		self.storeFtpFiles(fileList)
		print('create all files')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.FTP_DOWNLOADING_RECEIVED, None))
		
	def createDirectory(self, directoryName):
		print('create directory: ', directoryName)
		if not os.path.exists(directoryName):
			os.mkdir(directoryName)
			
	def storeFtpFiles(self, fileList):
		for fileName in fileList:
			self.storeFtpFile(fileName)
			
	def storeFtpFile(self, fileName):
		print('create file: ', fileName)
		f = open(fileName, 'wb')
		ClientData.ftp.retrbinary('RETR ' + fileName, f.write) 
		f.close()