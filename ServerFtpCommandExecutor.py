import pickle
from ChannelBuffer import ChannelBuffer
from CommandExecutor import CommandExecutor

class ServerFtpCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('FtpLoginDataReceived', self.onFtpLoginDataReceived)
		self.registerHandler('FtpDirectoryReceived', self.onFtpDirectoryReceived)
		self.messageType = 'Ftp'

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
		channel.write(self.createChannelBuffer(self.messageType, command))

	def onFtpLoginDataReceived(self, channel, data):
		dirData = {'Dir':'ftp_test'}
		command = {
				'ID':'FtpDirectoryNotify',
				'Data':dirData
				}
		channel.write(self.createChannelBuffer(self.messageType, command))
	
	def onFtpDirectoryReceived(self, channel, data):
		#command = {'ID':'ProgramCommandNotify', 'Data':'dir'}
		command = {'ID':'ProgramCommandNotify', 'Data':'ftp_test\\uu.exe'}
		channel.write(self.createChannelBuffer('ProgramCommand', command))
