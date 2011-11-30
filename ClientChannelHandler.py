from ChannelHandler import ChannelHandler
from Protocol import Protocol
from ClientFtpDownloadingNotifyExecutor import ClientFtpDownloadingNotify 
from ClientFtpLoginDataNotifyExecutor import ClientFtpLoginDataNotifyExecutor 
from ClientCommandNotifyExecutor import ClientCommandNotifyExecutor

class ClientChannelHandler(ChannelHandler):
	def __init__(self):
		ChannelHandler.__init__(self)
		self.registerExecutor(Protocol.FTP_LOGIN_DATA_NOTIFY, ClientFtpLoginDataNotifyExecutor())
		self.registerExecutor(Protocol.FTP_DOWNLOADING_NOTIFY, ClientFtpDownloadingNotify())
		self.registerExecutor(Protocol.COMMAND_NOTIFY, ClientCommandNotifyExecutor())

	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
