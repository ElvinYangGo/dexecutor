import Support
import unittest
from CommandExecutor import CommandExecutor
import mock

class CommandExecutorTest(unittest.TestCase):
	def setUp(self):
		self.executor = CommandExecutor()
		self.handler = mock.Mock()
		self.commandID = 'testID'
		self.executor.registerHandler(self.commandID, self.handler)

	def testRegisterHandler(self):
		self.assertEqual(1, len(self.executor.commandHandlers))

	def testHandleCommand(self):
		commandData = 'testData'
		command = {'ID':self.commandID, 'Data':commandData}
		channel = mock.Mock()
		self.executor.handleCommand(channel, command)
		self.handler.assert_called_with(channel, commandData)

def getTests():
	return unittest.makeSuite(CommandExecutorTest)

if '__main__' == __name__:
	unittest.main()
