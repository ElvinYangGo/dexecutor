import Support
import unittest
from BufferHeadEncoder import BufferHeadEncoder
from ChannelBuffer import ChannelBuffer
import struct

class BufferHeadEncoderTest(unittest.TestCase):
	def testEncode(self):
		stringBytes = bytes('abcde', 'utf8')
		channelBuffer = ChannelBuffer(stringBytes)

		buffer = struct.pack('!i' + str(len(stringBytes)) + 's', len(stringBytes), stringBytes)
		encoder = BufferHeadEncoder()
		channelBufferToCheck = encoder.handleDownStream(channelBuffer)
		self.assertEqual(buffer, channelBufferToCheck.getAllBytes())

def getTests():
	return unittest.makeSuite(BufferHeadEncoderTest)

if '__main__' == __name__:
	unittest.main()

