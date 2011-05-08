import pickle
from ChannelHandler import ChannelHandler
from Channel import Channel
from ChannelBuffer import ChannelBuffer
from ServerFtpCommandExecutor import ServerFtpCommandExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		self.serverFtpCommandExuector = ServerFtpCommandExecutor()

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		self.serverFtpCommandExuector.sendFtpLoginData(channel)
		"""
		ftpData = {
				'ip':'127.0.0.1', 
				'port':21,
				'userName':'test',
				'password':'test'
				}
		command = {
				'ID':'FtpData',
				'Data':ftpData
				}
		message = {
				'Type':'Ftp',
				'Command':command
				}
		pickleBytes = pickle.dumps(message)
		channel.write(ChannelBuffer(pickleBytes))
		"""

	def messageReceived(self, channel, channelBuffer):
		data = channelBuffer.readAllBytes().decode('utf8')
		print(data)
		channel.write(ChannelBuffer(bytes(data, 'utf8')))

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
