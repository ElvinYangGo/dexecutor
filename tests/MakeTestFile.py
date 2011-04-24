import sys

if '__main__' == __name__:
	fileName = sys.argv[1]
	testFile = open(fileName+'.py', 'w')

	testFile.write('import Support\n')
	testFile.write('import unittest\n')
	testFile.write('from ' + fileName + ' import ' + fileName + '\n\n')

	testFile.write('class ' + fileName + '(unittest.TestCase):\n')
	testFile.write('	pass\n\n')

	testFile.write('def getTests():\n')
	testFile.write('	return unittest.makeSuite(' + fileName + ')\n\n')

	testFile.write("if '__main__' == __name__:\n")
	testFile.write('	unittest.main()')

	testFile.close()
