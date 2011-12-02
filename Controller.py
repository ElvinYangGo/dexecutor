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
		command = {'ID':Protocol.CONTROLLER_COMMAND_NOTIFY, 'Data':inputData}
		channel.write(ChannelBufferFactory.createChannelBuffer(command))
		print('send: ', inputData)

		
