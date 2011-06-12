from CommandExecutor import CommandExecutor
import os

class ClientProgramCommandExecutor(CommandExecutor):
	def __init__(self):
		CommandExecutor.__init__(self)
		self.registerHandler('ListDirectory', self.programCommandReceived)

	def programCommandReceived(self, channel, programData):
		#command = {'ID':'ListDirectory', 'Data':'dir'}
		print('.............................')
		os.system(programData)
