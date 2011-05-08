import pickle
from ChannelHandler import ChannelHandler
from Channel import Channel
from ChannelBuffer import ChannelBuffer

class ServerChannelHandler(ChannelHandler):
	def channelConnected(self, channel):
		print(channel.getAddress(), ' connected')
		ftpData = {
				'ip':'127.0.0.1', 
				'port':21,
				'userName':'test',
				'password':'test'
				}
		message = {
				'ID':'FtpData',
				'Data':ftpData
				}
		pickleBytes = pickle.dumps(message)
		channel.write(ChannelBuffer(pickleBytes))

	def messageReceived(self, channel, channelBuffer):
		data = channelBuffer.readAllBytes().decode('utf8')
		print(data)
		channel.write(ChannelBuffer(bytes(data, 'utf8')))

	def channelClosed(self, channel):
		print(channel.getAddress(), ' closed')
