import pickle
from ChannelBuffer import ChannelBuffer

class ServerFtpCommandExecutor:
	def sendFtpLoginData(self, channel):
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

