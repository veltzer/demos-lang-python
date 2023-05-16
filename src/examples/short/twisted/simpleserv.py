"""
A simple twisted server doing echo on two ports.
"""

from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol
    As soon as any data is received,write it back."""
    def __init__(self):
        super().__init__(self)

    def dataReceived(self, data):
        self.transport.write(data)


factory = protocol.ServerFactory()
factory.protocol = Echo

# This runs the protocol on port 8000
# pylint: disable=no-member
reactor.listenTCP(8000, factory)  # type: ignore
# And again on port 8002
# pylint: disable=no-member
reactor.listenTCP(8002, factory)  # type: ignore
# run the main loop of the reactor
# pylint: disable=no-member
reactor.run()  # type: ignore
