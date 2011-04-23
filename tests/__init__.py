import os
import sys
import unittest

def getTests():
	currentDirectory = os.path.abspath(os.path.dirname(sys.argv[0]))
	suite = unittest.TestSuite()
	for fileName in os.listdir(currentDirectory):
		if fileName.startswith('test') and fileName.endswith('.py'):
			moduleName = fileName[:-3]
			__import__(moduleName)
			module = sys.modules[moduleName]
			suite.addTest(module.getTests())

	return suite

if '__main__' == __name__:
	suite = getTests()
	runner = unittest.TextTestRunner()
	runner.run(suite)
