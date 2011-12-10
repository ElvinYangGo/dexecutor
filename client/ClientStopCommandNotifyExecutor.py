from common.CommandExecutor import CommandExecutor
import traceback
from client import ClientData
from common.ChannelBufferFactory import ChannelBufferFactory
from common.Protocol import Protocol

class ClientStopCommandNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print(data)
		try:
			ClientData.childProcess.terminate()
			print('stop command')
		except BaseException:
			traceback.print_exc()
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.STOP_COMMAND_RECEIVED, None))	
