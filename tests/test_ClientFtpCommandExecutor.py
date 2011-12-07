import Support
import unittest
from ClientFtpCommandExecutor import ClientFtpCommandExecutor
from mock import Mock
import os
import ftplib

class ClientFtpCommandExecutorTest(unittest.TestCase):
	def setUp(self):
		self.channel = Mock()
		self.ftpData = {
				'IP':'127.0.0.1', 
				'Port':21,
				'UserName':'test',
				'Password':'test'
				}
		self.ftpHandler = ftplib.FTP(self.ftpData['IP'], self.ftpData['UserName'], self.ftpData['Password'])
		self.clientFtpCommandExecutor = ClientFtpCommandExecutor()
		self.clientFtpCommandExecutor.ftpHandler = self.ftpHandler

	def testOnFtpDirectoryNotify(self):
		dirData = {'Dir':'ftp_test'}
		self.clientFtpCommandExecutor.onFtpDirectoryNotify(self.channel, dirData)
		self.assertTrue(os.path.exists('ftp_test'))

	def testCreateDirectory(self):
		directoryName = 'ftp_test'
		self.clientFtpCommandExecutor.createDirectory(directoryName)
		self.assertTrue(os.path.exists(directoryName))

	def testStoreFtpFiles(self):
		fileAName = 'ftp_test\\a.txt'
		fileBName = 'ftp_test\\b.txt'
		fileList = [fileAName, fileBName]
		self.clientFtpCommandExecutor.saveFtpFiles(fileList)
		fileA = open(fileAName, 'r')
		fileB = open(fileBName, 'r')
		fileA.close()
		fileB.close()

	def testStoreFtpFile(self):
		fileName = 'ftp_test\\a.txt'
		self.clientFtpCommandExecutor.saveFtpFile(fileName)
		f = open('ftp_test\\a.txt', 'r')
		f.close()

def getTests():
	return unittest.makeSuite(ClientFtpCommandExecutorTest)

if '__main__' == __name__:
	unittest.main()
