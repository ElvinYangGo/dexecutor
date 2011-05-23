import pickle
from ChannelBuffer import ChannelBuffer
from FtpCommandExecutor import FtpCommandExecutor

class ServerFtpCommandExecutor(FtpCommandExecutor):
	def handleCommand(self, channel, command):
		if command['ID'] == 'FtpLoginDataReceived':
			self.ftpLoginDataReceived(channel)

	def sendFtpLoginData(self, channel):
		ftpData = {
				'IP':'127.0.0.1', 
				'Port':21,
				'UserName':'test',
				'Password':'test'
				}
		command = {
				'ID':'FtpLoginDataNotify',
				'Data':ftpData
				}
		channel.write(self.createChannelBuffer(command))

	def ftpLoginDataReceived(self, channel):
		print('client received ftp login data')
		dirData = {'Dir':'test'}
		command = {
				'ID':'FtpFolderNotify',
				'Data':dirData
				}
		channel.write(self.createChannelBuffer(command))
