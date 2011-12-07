from ChannelHandler import ChannelHandler
from Protocol import Protocol
from ServerFtpLoginDataReceivedExecutor import ServerFtpLoginDataReceivedExecutor
from ServerFtpDownloadReceivedExecutor import ServerFtpDownloadReceivedExecutor
from ServerCommandReceivedExecutor import ServerCommandReceivedExecutor
from ServerControllerCommandExecutor import ServerControllerCommandExecutor
from ServerFtpUploadReceivedExecutor import ServerFtpUploadReceivedExecutor
from ServerConfigReceivedExecutor import ServerConfigReceivedExecutor
from ChannelBufferFactory import ChannelBufferFactory

class ServerChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_RECEIVED, ServerFtpLoginDataReceivedExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOAD_RECEIVED, ServerFtpDownloadReceivedExecutor())
		self.registerExecutor(Protocol.FTP_UPLOAD_NOTIFY, ServerFtpUploadReceivedExecutor())
		self.registerExecutor(Protocol.COMMAND_RECEIVED, ServerCommandReceivedExecutor())
		self.registerExecutor(Protocol.CONTROLLER_COMMAND_NOTIFY, ServerControllerCommandExecutor())
		self.registerExecutor(Protocol.CONFIG_RECEIVED, ServerConfigReceivedExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.CONFIG_NOTIFY, channel.getID()))

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
