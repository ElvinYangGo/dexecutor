from ClientBootstrap import ClientBootstrap
from ChannelPipelineFactory import ChannelPipelineFactory
from ControllerChannelHandler import ControllerChannelHandler 
from Protocol import Protocol
from ChannelBufferFactory import ChannelBufferFactory
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

		
