import pickle
from ChannelBuffer import ChannelBuffer
from CommandExecutor import CommandExecutor

class ServerFtpCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('FtpLoginDataReceived', self.ftpLoginDataReceived)

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
		channel.write(self.createChannelBuffer('Ftp', command))

	def ftpLoginDataReceived(self, channel, data):
		print('client received ftp login data')
		dirData = {'Dir':'test'}
		command = {
				'ID':'FtpDirectoryNotify',
				'Data':dirData
				}
		channel.write(self.createChannelBuffer('Ftp', command))
