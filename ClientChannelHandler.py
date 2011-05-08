import pickle
import ftplib
from ChannelHandler import ChannelHandler
from ChannelBuffer import ChannelBuffer
from Channel import Channel
from ClientFtpCommandExecutor import ClientFtpCommandExecutor

class ClientChannelHandler(ChannelHandler):
	def __init__(self):
		self.clientFtpCommandExecutor = ClientFtpCommandExecutor()

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def messageReceived(self, channel, channelBuffer):
		message = pickle.loads(channelBuffer.readAllBytes())
		print(message)
		if message['Type'] == 'Ftp':
			self.clientFtpCommandExecutor.handleCommand(channel, message['Command'])
	
	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
