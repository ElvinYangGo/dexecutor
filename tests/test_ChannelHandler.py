import Support
import unittest
from ChannelHandler import ChannelHandler
from Channel import Channel

class ChannelHandlerTest(unittest.TestCase):
	def setUp(self):
		self.sock = 123
		self.address = ('127.0.0.1', 23567)
		self.channel = Channel(self.sock, self.address)

	def testMessageReceived(self):
		pass

	def testChannelConnected(self):
		channelHandler = ChannelHandler()
		channelHandler.channelConnected(self.channel)

def getTests():
	return unittest.makeSuite(ChannelHandlerTest)

if '__main__' == __name__:
	unittest.main()
