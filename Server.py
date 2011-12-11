from server.ServerBootstrap import ServerBootstrap
from server.ServerChannelPipelineFactory import ServerChannelPipelineFactory
from common.ChannelManager import ChannelManager
import time

if '__main__' == __name__:
	channelManager = ChannelManager()
	serverChannelPipelineFactory = ServerChannelPipelineFactory(channelManager)
	serverBootstrap = ServerBootstrap(channelManager)
	serverBootstrap.setPipelineFactory(serverChannelPipelineFactory)
	serverBootstrap.bindServer('localhost', 23567)
	while True:
		serverBootstrap.serveOnce()

		try:
			time.sleep(0.5)
		except KeyboardInterrupt:
			print('interrupt')
			break
	print('shutdown')
