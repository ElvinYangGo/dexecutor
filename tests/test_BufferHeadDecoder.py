import Support
import unittest
from BufferHeadDecoder import BufferHeadDecoder
from BufferHeadEncoder import BufferHeadEncoder
from ChannelBuffer import ChannelBuffer
import struct

class BufferHeadDecoderTest(unittest.TestCase):
	def testDecode(self):
		stringBytes = bytes('abcde', 'utf8')
		encoder = BufferHeadEncoder()
		channelBufferEncoded = encoder.handleDownStream(ChannelBuffer(stringBytes))

		decoder = BufferHeadDecoder()
		channelBufferDecoded = decoder.handleUpStream(channelBufferEncoded)
		self.assertEqual(stringBytes, channelBufferDecoded.getAllBytes())
		self.assertEqual(0, channelBufferEncoded.readableBytes())

def getTests():
	return unittest.makeSuite(BufferHeadDecoderTest)

if '__main__' == __name__:
	unittest.main()

