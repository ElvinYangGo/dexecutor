from common.CommandExecutor import CommandExecutor
import client.ClientData
from common.ChannelBufferFactory import ChannelBufferFactory
from common.Protocol import Protocol

class ClientFtpLoginDataNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		client.ClientData.ftpLoginData = data
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.FTP_LOGIN_DATA_RECEIVED, None))
