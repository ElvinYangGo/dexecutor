import Support
import unittest
from ServerProgramCommandExecutor import ServerProgramCommandExecutor
import mock

class ServerProgramCommandExecutorTest(unittest.TestCase):
	def setUp(self):
		self.serverProgramCommandExecutor = ServerProgramCommandExecutor()

	def testConstructor(self):
		self.assertEqual(0, len(self.serverProgramCommandExecutor.commandHandlers))
	
	def testSendProgramCommand(self):
		self.serverProgramCommandExecutor.createChannelBuffer = mock.Mock()
		channel = mock.Mock()
		channel.write = mock.Mock()
		self.serverProgramCommandExecutor.sendProgramCommand(channel)
		command = {'ID':'ListDirectory', 'Data':'dir'}
		self.serverProgramCommandExecutor.createChannelBuffer.assert_called_with('ProgramCommand', command)

def getTests():
	return unittest.makeSuite(ServerProgramCommandExecutorTest)

if '__main__' == __name__:
	unittest.main()
