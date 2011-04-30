import Support
import unittest
from ChannelPipelineFactory import ChannelPipelineFactory
from ChannelHandler import ChannelHandler

class ChannelPipelineFactoryTest(unittest.TestCase):
	def testConstructor(self):
		channelPipelineFactory = ChannelPipelineFactory(ChannelHandler())
		self.assertEqual(1, channelPipelineFactory.handlerCount())

def getTests():
	return unittest.makeSuite(ChannelPipelineFactoryTest)

if '__main__' == __name__:
	unittest.main()
