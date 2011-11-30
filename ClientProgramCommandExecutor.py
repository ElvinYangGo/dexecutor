from CommandExecutor import CommandExecutor
import subprocess

class ClientProgramCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('ProgramCommandNotify', self.onProgramCommandNotify)

	def onProgramCommandNotify(self, channel, programData):
		print(programData)
		subprocess.Popen(programData)
