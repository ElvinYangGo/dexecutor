import Support
import unittest
from mock import Mock
import Stdio

class StdioTest(unittest.TestCase):
	def setUp(self):
		"""
		self.mockStdin = Mock()
		self.mockStdin.readline.return_value = 'aaaaaaa' 
		self.originalStdin = sys.stdin
		sys.stdin = self.mockStdin
		"""

	def tearDown(self):
		pass
		#sys.stdin = self.originalStdin

	"""
	def testreadline(self):
		pass
		stdio = Stdio.Stdio()
		s = stdio.read()
		self.assertEqual('aaa', s)
	"""

def getTests():
	return unittest.makeSuite(StdioTest)

if __name__ == '__main__':
	unittest.main()

