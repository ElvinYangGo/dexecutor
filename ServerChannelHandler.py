from ChannelHandler import ChannelHandler
from Protocol import Protocol
from ServerFtpLoginDataReceivedExecutor import ServerFtpLoginDataReceivedExecutor
from ServerFtpDownloadingReceivedExecutor import ServerFtpDownloadingReceivedExecutor
from ServerCommandReceivedExecutor import ServerCommandReceivedExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_RECEIVED, ServerFtpLoginDataReceivedExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOADING_RECEIVED, ServerFtpDownloadingReceivedExecutor())
		self.registerExecutor(Protocol.COMMAND_RECEIVED, ServerCommandReceivedExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		#self.sendProgramCommand(channel)

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
	"""
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
		channel.write(ChannelBufferFactory.createChannelBuffer('Ftp', command))

	def sendProgramCommand(self, channel):
		command = {'ID':'ProgramCommandNotify', 'Data':'cmd.exe /c dir'}
		channel.write(ChannelBufferFactory.createChannelBuffer('ProgramCommand', command))
	"""