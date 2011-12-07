from CommandExecutor import CommandExecutor
import ClientData
from ChannelBufferFactory import ChannelBufferFactory
from Protocol import Protocol

class ClientFtpLoginDataNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		ClientData.ftpLoginData = data
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.FTP_LOGIN_DATA_RECEIVED, None))
