import pickle
import ftplib
from ChannelHandler import ChannelHandler
from ChannelBuffer import ChannelBuffer
from Channel import Channel
from ClientFtpCommandExecutor import ClientFtpCommandExecutor
from ClientProgramCommandExecutor import ClientProgramCommandExecutor

class ClientChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.clientFtpCommandExecutor = ClientFtpCommandExecutor()
		self.clientProgramCommandExecutor = ClientProgramCommandExecutor()
		self.registerExecutor('Ftp', self.clientFtpCommandExecutor)
		self.registerExecutor('ProgramCommand', self.clientProgramCommandExecutor)

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
