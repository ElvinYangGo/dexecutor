from CommandExecutor import CommandExecutor
import subprocess
import traceback

class ClientCommandNotifyExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		
	def onMessage(self, channel, data):
		print(data)
		try:
			subprocess.Popen(data)
		except BaseException:
			traceback.print_exc()
			
