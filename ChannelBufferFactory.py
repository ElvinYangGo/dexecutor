from ChannelBuffer import ChannelBuffer
import pickle

class ChannelBufferFactory:
	def createMessage(messageType, command):
		message = {
				'Type':messageType,
				'Command':command
				}
		return message

	def createChannelBuffer(messageType, command):
		pickleBytes = pickle.dumps(ChannelBufferFactory.createMessage(messageType, command))
		return ChannelBuffer(pickleBytes)
