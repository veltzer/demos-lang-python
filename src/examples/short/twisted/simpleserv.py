"""
A simple twisted server doing echo on two ports.
"""

from twisted.internet import reactor, protocol

'''This is just about the simplest possible protocol
As soon as any data is received,write it back.'''


class Echo(protocol.Protocol):
    def __init__(self):
        super(Echo, self).__init__()

    def dataReceived(self, data):
        self.transport.write(data)


factory = protocol.ServerFactory()
factory.protocol = Echo

'''This runs the protocol on port 8000'''
reactor.listenTCP(8000, factory)
'''And again on port 8002'''
reactor.listenTCP(8002, factory)
'''run the main loop of the reactor'''
reactor.run()
