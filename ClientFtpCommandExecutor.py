import ftplib

class ClientFtpCommandExecutor:
	def handleCommand(self, channel, command):
		if command['ID'] == 'FtpData':
			self.ftpDataReceived(channel, command['Data'])

	def ftpDataReceived(self, channel, ftpData):
		ftpHandler = ftplib.FTP(ftpData['ip'], ftpData['userName'], ftpData['password'])
		fileList = ftpHandler.nlst()
		print(fileList)

