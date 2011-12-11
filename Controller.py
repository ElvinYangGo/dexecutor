from client.ClientBootstrap import ClientBootstrap
from controller.ControllerChannelPipelineFactory import ControllerChannelPipelineFactory
from common.Protocol import Protocol
from common.ChannelBufferFactory import ChannelBufferFactory
import sys

if '__main__' == __name__:
	controllerChannelPipelineFactory = ControllerChannelPipelineFactory()
	clientBootstrap = ClientBootstrap()
	clientBootstrap.setPipelineFactory(controllerChannelPipelineFactory)
	channel = clientBootstrap.connect('localhost', 23567)
	while True:
		clientBootstrap.serveOnce()
		inputData = sys.stdin.readline()
		inputData = inputData.replace('\n', '')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.CONTROLLER_COMMAND_NOTIFY, inputData))

		
