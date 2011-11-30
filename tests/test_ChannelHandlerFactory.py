import Support
import unittest
from ChannelHandlerFactory import ChannelHandlerFactory
from ChannelHandler import ChannelHandler
from ClientChannelHandler import ClientChannelHandler
from ServerProgramCommandExecutor import ServerProgramCommandExecutor

class ChannelHandlerFactoryTest(unittest.TestCase):
	def setUp(self):
		self.channelHandlerFactory = ChannelHandlerFactory(ClientChannelHandler)
		self.channelHandlerFactory.registerExecutor('ProgramCommand', ServerProgramCommandExecutor())
		
	def testConstructor(self):
		self.assertEqual(1, self.channelHandlerFactory.handlerCount())

	def testCreateChannelHandler(self):
		channelHandler = self.channelHandlerFactory.createChannelHandler()
		channelHandler2 = self.channelHandlerFactory.createChannelHandler()
		print(channelHandler)
		print(channelHandler2)
		self.assertTrue(isinstance(channelHandler, ChannelHandler))
		self.assertEqual(1, channelHandler.handlerCount())

def getTests():
	return unittest.makeSuite(ChannelHandlerFactoryTest)

if '__main__' == __name__:
	unittest.main()
