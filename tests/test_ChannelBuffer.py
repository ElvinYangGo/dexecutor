import Support
import unittest
from ChannelBuffer import ChannelBuffer
import struct

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

	def testGetPacketSize(self):
		dataSize = 22
		sizeBuffer = struct.pack('!i', dataSize)
		self.buffer.append(sizeBuffer)
		self.assertEqual(dataSize, self.buffer.getPacketSize())

	def testGetPacketSize2(self):
		s = 'abcde'
		stringBytes = bytes(s, 'utf8')
		packet = struct.pack('!i' + str(len(stringBytes)) + 's', len(stringBytes), stringBytes)
		self.buffer.append(packet)
		self.assertEqual(len(packet), self.buffer.readableBytes())

	def testExtractPacket(self):
		s = 'abcde'
		stringBytes = bytes(s, 'utf8')
		data = struct.pack('!i' + str(len(stringBytes)) + 's', 999, stringBytes)
		packetToAppend = struct.pack('!i' + str(len(data)) + 's', len(data), data)
		self.buffer.append(packetToAppend)

		dataToCheck = self.buffer.extractPacket()
		self.assertEqual(data, dataToCheck)
		self.assertEqual(0, self.buffer.readableBytes())

		integerParam, stringParam = struct.unpack('!i'


def getTests():
	return unittest.makeSuite(ChannelBufferTest)

if '__main__' == __name__:
	unittest.main()
