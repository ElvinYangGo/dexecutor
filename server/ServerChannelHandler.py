from common.ChannelHandler import ChannelHandler
from common.Protocol import Protocol
from common.ChannelBufferFactory import ChannelBufferFactory
from server.ServerFtpLoginDataReceivedExecutor import ServerFtpLoginDataReceivedExecutor
from server.ServerFtpDownloadReceivedExecutor import ServerFtpDownloadReceivedExecutor
from server.ServerRunCommandReceivedExecutor import ServerRunCommandReceivedExecutor 
from server.ServerControllerCommandExecutor import ServerControllerCommandExecutor
from server.ServerFtpUploadReceivedExecutor import ServerFtpUploadReceivedExecutor
from server.ServerConfigReceivedExecutor import ServerConfigReceivedExecutor
from server.ServerStopCommandReceivedExecutor import ServerStopCommandReceivedExecutor

class ServerChannelHandler(ChannelHandler):
	def __init__(self, channelManager):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_RECEIVED, ServerFtpLoginDataReceivedExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOAD_RECEIVED, ServerFtpDownloadReceivedExecutor())
		self.registerExecutor(Protocol.FTP_UPLOAD_NOTIFY, ServerFtpUploadReceivedExecutor())
		self.registerExecutor(Protocol.RUN_COMMAND_RECEIVED, ServerRunCommandReceivedExecutor())
		self.registerExecutor(Protocol.STOP_COMMAND_RECEIVED, ServerStopCommandReceivedExecutor())
		self.registerExecutor(Protocol.CONTROLLER_COMMAND_NOTIFY, ServerControllerCommandExecutor(channelManager))
		self.registerExecutor(Protocol.CONFIG_RECEIVED, ServerConfigReceivedExecutor())

	def handleConnected(self, channel):
		print(channel.getAddress(), ' connected')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.CONFIG_NOTIFY, channel.getID()))

	def handleDisconnected(self, channel):
		print(channel.getAddress(), ' closed')
