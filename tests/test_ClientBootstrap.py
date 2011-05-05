import Support
import unittest
from ClientBootstrap import ClientBootstrap

class ClientBootstrapTest(unittest.TestCase):
	pass

def getTests():
	return unittest.makeSuite(ClientBootstrapTest)

if '__main__' == __name__:
	unittest.main()