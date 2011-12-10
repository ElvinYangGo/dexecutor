from common.ChannelHandler import ChannelHandler
from common.Protocol import Protocol
from client.ClientFtpDownloadNotifyExecutor import ClientFtpDownloadNotify 
from client.ClientFtpLoginDataNotifyExecutor import ClientFtpLoginDataNotifyExecutor 
from client.ClientRunCommandNotifyExecutor import ClientRunCommandNotifyExecutor
from client.ClientFtpUploadNotifyExecutor import ClientFtpUploadNotify
from client.ClientConfigNotifyExecutor import ClientConfigNotifyExecutor
from client.ClientStopCommandNotifyExecutor import ClientStopCommandNotifyExecutor

class ClientChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_NOTIFY, ClientFtpLoginDataNotifyExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOAD_NOTIFY, ClientFtpDownloadNotify())
		self.registerExecutor(Protocol.FTP_UPLOAD_NOTIFY, ClientFtpUploadNotify())
		self.registerExecutor(Protocol.RUN_COMMAND_NOTIFY, ClientRunCommandNotifyExecutor())
		self.registerExecutor(Protocol.STOP_COMMAND_NOTIFY, ClientStopCommandNotifyExecutor())
		self.registerExecutor(Protocol.CONFIG_NOTIFY, ClientConfigNotifyExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
