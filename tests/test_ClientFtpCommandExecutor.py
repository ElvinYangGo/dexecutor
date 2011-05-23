import Support
import unittest
from ClientFtpCommandExecutor import ClientFtpCommandExecutor
from mock import Mock

class ClientFtpCommandExecutorTest(unittest.TestCase):
	def testHandleCommand(self):
		ftpData = {
				'IP':'127.0.0.1', 
				'Port':21,
				'UserName':'test',
				'Password':'test'
				}
		command = {
				'ID':'FtpLoginDataNotify',
				'Data':ftpData
				}
		channel = Mock()
		clientFtpCommandExecutor = ClientFtpCommandExecutor()
		clientFtpCommandExecutor.ftpLoginDataReceived = Mock()
		clientFtpCommandExecutor.registerHandler('FtpLoginDataNotify', clientFtpCommandExecutor.ftpLoginDataReceived)
		clientFtpCommandExecutor.handleCommand(channel, command)
		clientFtpCommandExecutor.ftpLoginDataReceived.assert_called_with(channel, command['Data'])

def getTests():
	return unittest.makeSuite(ClientFtpCommandExecutorTest)

if '__main__' == __name__:
	unittest.main()
