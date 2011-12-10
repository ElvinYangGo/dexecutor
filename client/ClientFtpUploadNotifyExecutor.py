from common.CommandExecutor import CommandExecutor
from client import ClientData
import os
import ftplib
from common.Protocol import Protocol
from common.ChannelBufferFactory import ChannelBufferFactory

class ClientFtpUploadNotify(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		ClientData.ftp = ftplib.FTP(
			ClientData.ftpLoginData['IP'], 
			ClientData.ftpLoginData['UserName'], 
			ClientData.ftpLoginData['Password']
			)
		if os.path.isdir(data):
			directoryInFtpServer = data + '_' + str(ClientData.uniqueID)
			self.createDirectoryInFtpServer(data, directoryInFtpServer)
			self.uploadFiles(data, directoryInFtpServer)
		else:
			print(data)
			self.uploadFile(data)
			self.uploadFile(data, data + str(ClientData.uniqueID))
		
		print('upload all files')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.FTP_UPLOAD_RECEIVED, None))
	
	def uploadFile(self, fileName, fileNameInFtpServer):
		f = open(fileName, mode='rb')
		ClientData.ftp.storbinary('STOR ' + fileNameInFtpServer, f)
		f.close()
		
	def uploadFiles(self, data, directoryInFtpServer):
		originalPathInFtpServer = ClientData.ftp.pwd()
		ClientData.ftp.cwd(directoryInFtpServer)
		
		fileList = os.listdir(data)
		for fileName in fileList:
			filePath = os.path.join(data, fileName)
			self.uploadFile(filePath, fileName)
			print('upload: ' + filePath)
		ClientData.ftp.cwd(originalPathInFtpServer)
		
	def createDirectoryInFtpServer(self, data, directoryInFtpServer):
		fileListInFtpServer = ClientData.ftp.nlst()
		if directoryInFtpServer in fileListInFtpServer:
			fileList = ClientData.ftp.nlst(directoryInFtpServer)
			for fileName in fileList:
				ClientData.ftp.delete(fileName)
			print('remove all files in ftp server directory: ', directoryInFtpServer)
		else:
			ClientData.ftp.mkd(directoryInFtpServer)
			print('create directory in ftp server: ', directoryInFtpServer)
