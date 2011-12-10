from common.CommandExecutor import CommandExecutor
import subprocess
import traceback
from client import ClientData

class ClientRunCommandNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print(data)
		try:
			ClientData.childProcess = subprocess.Popen(data)
			print('execute command')
		except BaseException:
			traceback.print_exc()
			
