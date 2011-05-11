import pickle
from ChannelBuffer import ChannelBuffer

class FtpCommandExecutor:
	def createMessage(self, command):
		message = {
				'Type':'Ftp',
				'Command':command
				}
		return message 

	def createChannelBuffer(self, command):
		pickleBytes = pickle.dumps(self.createMessage(command))
		return ChannelBuffer(pickleBytes)

