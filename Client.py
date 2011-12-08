from ClientBootstrap import ClientBootstrap
from ChannelPipelineFactory import ChannelPipelineFactory
from ClientChannelHandler import ClientChannelHandler

if '__main__' == __name__:
	clientBootstrap = ClientBootstrap()
	clientBootstrap.setPipelineFactory(ChannelPipelineFactory(ClientChannelHandler()))
	clientBootstrap.connect('localhost', 23567)
	while True:
		clientBootstrap.serveOnce()
