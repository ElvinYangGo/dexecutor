import Support
import unittest
from ChannelPipeline import ChannelPipeline
from ChannelHandler import ChannelHandler
from Channel import Channel

class ChannelPipelineTest(unittest.TestCase):
	def setUp(self):
		self.sock = 123
		self.address = ('127.0.0.1', 23567)
		self.channel = Channel(self.sock, self.address)
		self.channelPipeline = ChannelPipeline((ChannelHandler(),))
		self.channelPipeline.setChannel(self.channel)
		self.channel.setChannelPipeline(self.channelPipeline)

	def testConstructor(self):
		self.assertEqual(1, self.channelPipeline.handlerCount())

	def testHandleChannelConnected(self):
		self.channelPipeline.handleChannelConnected()

	def testHandleChannelClosed(self):
		self.channelPipeline.handleChannelClosed()

def getTests():
	return unittest.makeSuite(ChannelPipelineTest)

if '__main__' == __name__:
	unittest.main()
