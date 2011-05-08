import Support
import unittest
from ServerChannelHandler import ServerChannelHandler

class ServerChannelHandlerTest(unittest.TestCase):
	pass

def getTests():
	return unittest.makeSuite(ServerChannelHandlerTest)

if '__main__' == __name__:
	unittest.main()