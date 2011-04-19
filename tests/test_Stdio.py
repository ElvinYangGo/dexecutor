import os
import sys

parent_path = os.path.join(os.path.dirname(sys.argv[0]), os.pardir)
absolute_parent_path = os.path.abspath(parent_path)
sys.path.append(absolute_parent_path)

import unittest
from mock import Mock
import Stdio

#print(dir(sys.stdin))
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

	def testreadline(self):
		stdio = Stdio.Stdio()
		s = stdio.read()
		self.assertEqual('aaa', s)

if __name__ == '__main__':
	unittest.main()

