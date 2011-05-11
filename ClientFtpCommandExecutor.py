import ftplib
import pickle
from ChannelBuffer import ChannelBuffer
from FtpCommandExecutor import FtpCommandExecutor

class ClientFtpCommandExecutor(FtpCommandExecutor):
	def handleCommand(self, channel, command):
		if command['ID'] == 'FtpLoginDataNotify':
			self.ftpLoginDataReceived(channel, command['Data'])

	def ftpLoginDataReceived(self, channel, ftpData):
		ftpHandler = ftplib.FTP(ftpData['IP'], ftpData['UserName'], ftpData['Password'])
		fileList = ftpHandler.nlst()
		print(fileList)
		command = {'ID':'FtpLoginDataReceived'}
		channel.write(self.createChannelBuffer(command))

