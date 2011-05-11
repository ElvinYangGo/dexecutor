import pickle
from ChannelHandler import ChannelHandler
from Channel import Channel
from ChannelBuffer import ChannelBuffer
from ServerFtpCommandExecutor import ServerFtpCommandExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		self.serverFtpCommandExecutor = ServerFtpCommandExecutor()

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		self.serverFtpCommandExecutor.sendFtpLoginData(channel)

	def messageReceived(self, channel, channelBuffer):
		message = pickle.loads(channelBuffer.readAllBytes())
		print(message)
		if message['Type'] == 'Ftp':
			self.serverFtpCommandExecutor.handleCommand(channel, message['Command'])

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
