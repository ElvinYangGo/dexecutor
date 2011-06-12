import Support
import unittest
from ClientProgramCommandExecutor import ClientProgramCommandExecutor

class ClientProgramCommandExecutorTest(unittest.TestCase):
	def testConstructor(self):
		clientProgramCommmandExecutor = ClientProgramCommandExecutor()
		self.assertEqual(1, len(clientProgramCommmandExecutor.commandHandlers))

def getTests():
	return unittest.makeSuite(ClientProgramCommandExecutorTest)

if '__main__' == __name__:
	unittest.main()
