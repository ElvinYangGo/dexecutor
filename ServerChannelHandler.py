import pickle
from ChannelHandler import ChannelHandler
from Channel import Channel
from ChannelBuffer import ChannelBuffer
from ServerFtpCommandExecutor import ServerFtpCommandExecutor
from ServerProgramCommandExecutor import ServerProgramCommandExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.serverFtpCommandExecutor = ServerFtpCommandExecutor()
		self.serverProgramCommandExecutor = ServerProgramCommandExecutor()
		self.registerExecutor('Ftp', self.serverFtpCommandExecutor)
		self.registerExecutor('ProgramCommand', self.serverFtpCommandExecutor)

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		self.serverFtpCommandExecutor.sendFtpLoginData(channel)
		#self.serverProgramCommandExecutor.sendProgramCommand(channel)

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
