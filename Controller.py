from client.ClientBootstrap import ClientBootstrap
from common.ChannelPipelineFactory import ChannelPipelineFactory
from controller.ControllerChannelHandler import ControllerChannelHandler 
from common.Protocol import Protocol
from common.ChannelBufferFactory import ChannelBufferFactory
import sys

if '__main__' == __name__:
	clientBootstrap = ClientBootstrap()
	clientBootstrap.setPipelineFactory(ChannelPipelineFactory(ControllerChannelHandler()))
	channel = clientBootstrap.connect('localhost', 23567)
	while True:
		clientBootstrap.serveOnce()
		inputData = sys.stdin.readline()
		inputData = inputData.replace('\n', '')
		channel.write(ChannelBufferFactory.createChannelBuffer(Protocol.CONTROLLER_COMMAND_NOTIFY, inputData))

		
