from ChannelBuffer import ChannelBuffer
import pickle

class ChannelBufferFactory:
	def createChannelBuffer(commandID, commandData):
		command = {'ID':commandID, 'Data':commandData}
		pickleBytes = pickle.dumps(command)
		return ChannelBuffer(pickleBytes)
