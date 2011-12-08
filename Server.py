from ServerBootstrap import ServerBootstrap
from ChannelPipelineFactory import ChannelPipelineFactory
from ServerChannelHandler import ServerChannelHandler
import time

if '__main__' == __name__:
	serverBootstrap = ServerBootstrap()
	serverBootstrap.setPipelineFactory(ChannelPipelineFactory(ServerChannelHandler()))
	serverBootstrap.bindServer('localhost', 23567)
	while True:
		serverBootstrap.serveOnce()

		try:
			time.sleep(0.5)
		except KeyboardInterrupt:
			print('interrupt')
			break
	print('shutdown')
