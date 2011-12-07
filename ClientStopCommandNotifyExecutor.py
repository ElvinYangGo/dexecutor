from CommandExecutor import CommandExecutor
import traceback
import ClientData
from ChannelBufferFactory import ChannelBufferFactory
from Protocol import Protocol

class ClientStopCommandNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print(data)
		try:
			ClientData.childProcess.terminate()
			#ClientData.childProcess.kill()
			print('stop command')
		except BaseException:
			traceback.print_exc()
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.STOP_COMMAND_RECEIVED, None))	
