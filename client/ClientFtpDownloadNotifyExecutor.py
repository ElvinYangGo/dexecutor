from common.CommandExecutor import CommandExecutor
import client.ClientData
import os
import ftplib
from common.Protocol import Protocol
from common.ChannelBufferFactory import ChannelBufferFactory

class ClientFtpDownloadNotify(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		client.ClientData.ftp = ftplib.FTP(
			client.ClientData.ftpLoginData['IP'], 
			client.ClientData.ftpLoginData['UserName'], 
			client.ClientData.ftpLoginData['Password']
			)
		self.createDirectory(data)
		fileList = client.ClientData.ftp.nlst(data)
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
		client.ClientData.ftp.retrbinary('RETR ' + fileName, f.write) 
		f.close()

