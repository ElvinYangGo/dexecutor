import Support
import unittest
from ChannelPipelineFactory import ChannelPipelineFactory
from ChannelHandler import ChannelHandler
from ChannelPipeline import ChannelPipeline

class ChannelPipelineFactoryTest(unittest.TestCase):
	def setUp(self):
		self.channelPipelineFactory = ChannelPipelineFactory(ChannelHandler())

	def testConstructor(self):
		self.assertEqual(1, self.channelPipelineFactory.handlerCount())

	def testCreateChannelPipeline(self):
		channelPipeline = self.channelPipelineFactory.createChannelPipeline()
		self.assertTrue(isinstance(channelPipeline, ChannelPipeline))
		self.assertEqual(1, channelPipeline.handlerCount())

def getTests():
	return unittest.makeSuite(ChannelPipelineFactoryTest)

if '__main__' == __name__:
	unittest.main()
