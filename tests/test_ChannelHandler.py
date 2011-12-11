import Support
import unittest
from ChannelHandler import ChannelHandler
from Channel import Channel
from ClientFtpCommandExecutor import ClientFtpCommandExecutor
from mock import Mock
import pickle
from ChannelBuffer import ChannelBuffer

class ChannelHandlerTest(unittest.TestCase):
	def setUp(self):
		self.channelHandler = ChannelHandler()
		self.ftpExecutor = Mock()
		self.ftpExecutor.handleCommand = Mock()
		self.channelHandler.registerExecutor('Ftp', self.ftpExecutor)

	def testRegisterExecutor(self):
		self.assertEqual(1, len(self.channelHandler.executors))

	def testMessageReceived(self):
		command = {'ID':'FtpLoginDataReceived'}
		message = {
				'Type':'Ftp',
				'Command':command
				}
		pickleBytes = pickle.dumps(message)
		channel = Mock()
		self.channelHandler.handleUpStream(channel, ChannelBuffer(pickleBytes))
		self.ftpExecutor.handleCommand.assert_called_with(channel, command)


def getTests():
	return unittest.makeSuite(ChannelHandlerTest)

if '__main__' == __name__:
	unittest.main()
