import pickle
from ChannelHandler import ChannelHandler
from Channel import Channel
from ChannelBuffer import ChannelBuffer
from ServerFtpCommandExecutor import ServerFtpCommandExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.serverFtpCommandExecutor = ServerFtpCommandExecutor()
		self.registerExecutor('Ftp', self.serverFtpCommandExecutor)

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		self.serverFtpCommandExecutor.sendFtpLoginData(channel)

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
