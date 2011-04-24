import Support
import unittest
from BufferHeadEncoder import BufferHeadEncoder
import struct

class BufferHeadEncoderTest(unittest.TestCase):
	def testEncode(self):
		stringBytes = bytes('abcde', 'utf8')
		buffer = struct.pack('!i' + str(len(stringBytes)) + 's', len(stringBytes), stringBytes)
		encoder = BufferHeadEncoder()
		bufferToCheck = encoder.encode(stringBytes)
		self.assertEqual(buffer, bufferToCheck)

def getTests():
	return unittest.makeSuite(BufferHeadEncoderTest)

if '__main__' == __name__:
	unittest.main()

