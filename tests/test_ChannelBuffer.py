import Support
import unittest
from ChannelBuffer import ChannelBuffer

class ChannelBufferTest(unittest.TestCase):
	def setUp(self):
		self.buffer = ChannelBuffer()

	def testReadableBytes(self):
		self.assertEqual(0, self.buffer.readableBytes())

	def testAppend(self):
		self.buffer.append(b'a')
		self.assertEqual(1, self.buffer.readableBytes())

		self.buffer.append(b'b')
		self.assertEqual(2, self.buffer.readableBytes())

	def testReadBytes(self):
		self.buffer.append(b'abcdefg')
		data = self.buffer.readBytes(4)
		self.assertEqual(data, bytearray(b'abcd'))
		self.assertEqual(3, self.buffer.readableBytes())

def getTests():
	return unittest.makeSuite(ChannelBufferTest)

if '__main__' == __name__:
	unittest.main()
