from ChannelHandler import ChannelHandler
from Protocol import Protocol
from ClientFtpDownloadNotifyExecutor import ClientFtpDownloadNotify 
from ClientFtpLoginDataNotifyExecutor import ClientFtpLoginDataNotifyExecutor 
from ClientCommandNotifyExecutor import ClientCommandNotifyExecutor
from ClientFtpUploadNotifyExecutor import ClientFtpUploadNotify
from ClientConfigNotifyExecutor import ClientConfigNotifyExecutor

class ClientChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_NOTIFY, ClientFtpLoginDataNotifyExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOAD_NOTIFY, ClientFtpDownloadNotify())
		self.registerExecutor(Protocol.FTP_UPLOAD_NOTIFY, ClientFtpUploadNotify())
		self.registerExecutor(Protocol.COMMAND_NOTIFY, ClientCommandNotifyExecutor())
		self.registerExecutor(Protocol.CONFIG_NOTIFY, ClientConfigNotifyExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
