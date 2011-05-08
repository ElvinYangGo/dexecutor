import pickle
import ftplib
from ChannelHandler import ChannelHandler
from ChannelBuffer import ChannelBuffer
from Channel import Channel

class ClientChannelHandler(ChannelHandler):
	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')

	def messageReceived(self, channel, channelBuffer):
		message = pickle.loads(channelBuffer.readAllBytes())
		print(message)
		if message['ID'] == 'FtpData':
			self.ftpDataReceived(message['Data'])
	
	def ftpDataReceived(self, ftpData):
		ftpHandler = ftplib.FTP(ftpData['ip'], ftpData['userName'], ftpData['password'])
		fileList = ftpHandler.nlst()
		print(fileList)

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
