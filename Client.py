from client.ClientBootstrap import ClientBootstrap
from common.ChannelPipelineFactory import ChannelPipelineFactory
from client.ClientChannelHandler import ClientChannelHandler

if '__main__' == __name__:
	clientBootstrap = ClientBootstrap()
	clientBootstrap.setPipelineFactory(ChannelPipelineFactory(ClientChannelHandler()))
	clientBootstrap.connect('localhost', 23567)
	while True:
		clientBootstrap.serveOnce()
