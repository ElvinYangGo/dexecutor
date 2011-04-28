import Support
import unittest
from ChannelBuffer import ChannelBuffer
from BufferHeadEncoder import BufferHeadEncoder
import struct

class ChannelBufferTest(unittest.TestCase):
	def setUp(self):
		self.buffer = ChannelBuffer()

	def testConstruct(self):
		data = bytes('abcde', 'utf8')
		bufferWithInitializedData = ChannelBuffer(data)
		self.assertEqual(len(data), bufferWithInitializedData.readableBytes())

	def testGetAllBytes(self):
		data = bytes('abcde', 'utf8')
		bufferWithInitializedData = ChannelBuffer(data)
		self.assertEqual(data, bufferWithInitializedData.getAllBytes())

	def testReadAllBytes(self):
		data = bytes('abcde', 'utf8')
		bufferWithInitializedData = ChannelBuffer(data)
		self.assertEqual(data, bufferWithInitializedData.readAllBytes())
		self.assertEqual(0, bufferWithInitializedData.readableBytes())
	
	def testGetBytes(self):
		data = struct.pack('!i', 999)
		bufferWithInitializedData = ChannelBuffer(data)
		self.assertEqual(data, bufferWithInitializedData.getBytes(struct.calcsize('!i')))

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
		self.assertEqual(data, b'abcd')
		self.assertEqual(3, self.buffer.readableBytes())

	def testSkipBytes(self):
		self.buffer.append(b'abcdefg')
		self.buffer.skipBytes(3)
		self.assertEqual(b'd', self.buffer.getBytes(1))
		self.assertEqual(4, self.buffer.readableBytes())

def getTests():
	return unittest.makeSuite(ChannelBufferTest)

if '__main__' == __name__:
	unittest.main()
