"""
solution.py
"""

import typing
from typing import Any

from twisted.internet import reactor
from twisted.internet.protocol import Factory, connectionDone
from twisted.protocols.basic import LineReceiver


class MyProtocol(LineReceiver):
    @typing.override
    def rawDataReceived(self, data: Any) -> None:  # pyrefly: ignore[bad-override]  twisted is replaced by Any in the project config, so pyrefly cannot see the LineReceiver parent method
        pass

    def __init__(self) -> None:
        self.name: str | None = None
        self.curFunc = self.handle_hello
        self.loggedIn = False

    def end(self, reason: str) -> None:
        self.transport.write("closing connection.\r\n")
        self.transport.write("reason is [" + reason + "]\r\n")
        self.transport.loseConnection()
        if self.loggedIn:
            self.factory.num_users -= 1
            self.loggedIn = False

    def handle_hello(self, line: str) -> None:
        if line == "hello":
            self.transport.write("hello\r\n")
            self.curFunc = self.handle_auth
        else:
            self.end("did not get hello")

    def handle_auth(self, line: str) -> None:
        (auth, name, password) = line.split(",")
        if auth == "auth":
            if name * 2 == password:
                self.transport.write("auth ok\r\n")
                self.curFunc = self.handle_status
                self.factory.num_users += 1
                self.name = name
                self.loggedIn = True
            else:
                self.end("authentication problem")
        else:
            self.end("did not get auth line")

    def handle_status(self, line: str) -> None:
        if line == "status":
            self.transport.write(
                "num_users is " + str(self.factory.num_users) + "\r\n")
            self.transport.write(f"your name is {self.name}\r\n")
            self.curFunc = self.handle_bye
        else:
            self.end("did not get status")

    def handle_bye(self, line: str) -> None:
        if line == "bye":
            self.transport.write(f"bye {self.name}\r\n")
            self.end("conversation ended")
        else:
            self.end("did not get bye")

    def connectionMade(self) -> None:
        print("connection made")
        self.transport.write("Welcome to MyServer\r\n")

    @typing.override
    def lineReceived(self, line: str) -> None:  # pyrefly: ignore[bad-override]  twisted is replaced by Any in the project config, so pyrefly cannot see the LineReceiver parent method
        print("got line ", line)
        self.curFunc(line)

    def connectionLost(self, reason: Any = connectionDone) -> None:
        print("connection was lost:", reason)
        if self.loggedIn:
            self.factory.num_users -= 1


class MyFactory(Factory):
    protocol = MyProtocol

    def __init__(self) -> None:
        self.num_users = 0
        self.port = 8007


my_factory = MyFactory()
reactor.listenTCP(my_factory.port, my_factory)
reactor.run()
