from client.ClientBootstrap import ClientBootstrap
from client.ClientChannelPipelineFactory import ClientChannelPipelineFactory

if '__main__' == __name__:
	clientChannelPippelineFactory = ClientChannelPipelineFactory()
	clientBootstrap = ClientBootstrap()
	clientBootstrap.setPipelineFactory(clientChannelPippelineFactory)
	clientBootstrap.connect('localhost', 23567)
	while True:
		clientBootstrap.serveOnce()
