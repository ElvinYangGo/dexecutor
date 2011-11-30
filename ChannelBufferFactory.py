from ChannelBuffer import ChannelBuffer
import pickle

class ChannelBufferFactory:
	def createChannelBuffer(command):
		pickleBytes = pickle.dumps(command)
		return ChannelBuffer(pickleBytes)
