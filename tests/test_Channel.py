import Support
import unittest
from Channel import Channel
from BufferHeadDecoder import BufferHeadDecoder
import struct

class ChannelTest(unittest.TestCase):
	def setUp(self):
		self.sock = 123
		self.address = ('127.0.0.1', 23567)
		self.channel = Channel(self.sock, self.address)

	def testGetAddress(self):
		self.assertEqual(self.address, self.channel.getAddress())
	
	def testGetSocket(self):
		self.assertEqual(self.sock, self.channel.getSocket())

	def testChannelBufferReadableBytes(self):
		self.assertEqual(0, self.channel.channelBufferReadableBytes())

	def testAppendBytes(self):
		self.channel.appendBytes(b'a')
		self.assertEqual(1, self.channel.channelBufferReadableBytes())
		self.channel.appendBytes(b'b')
		self.assertEqual(2, self.channel.channelBufferReadableBytes())
	
	#def testDecodeBuffer(self):


def getTests():
	return unittest.makeSuite(ChannelTest)

if '__main__' == __name__:
	unittest.main()

