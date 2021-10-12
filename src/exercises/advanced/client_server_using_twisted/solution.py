from twisted.internet import reactor
from twisted.internet.protocol import Factory, connectionDone
from twisted.protocols.basic import LineReceiver


class MyProtocol(LineReceiver):
    def rawDataReceived(self, data):
        pass

    def __init__(self):
        self.name = None
        self.curFunc = self.handle_hello
        self.loggedIn = False

    def end(self, reason):
        self.transport.write('closing connection.\r\n')
        self.transport.write('reason is [' + reason + ']\r\n')
        self.transport.loseConnection()
        if self.loggedIn:
            self.factory.num_users -= 1
            self.loggedIn = False

    def handle_hello(self, line):
        if line == 'hello':
            self.transport.write('hello\r\n')
            self.curFunc = self.handle_auth
        else:
            self.end('did not get hello')

    def handle_auth(self, line):
        (auth, name, password) = line.split(',')
        if auth == 'auth':
            if name * 2 == password:
                self.transport.write('auth ok\r\n')
                self.curFunc = self.handle_status
                self.factory.num_users += 1
                self.name = name
                self.loggedIn = True
            else:
                self.end('authentication problem')
        else:
            self.end('did not get auth line')

    def handle_status(self, line):
        if line == 'status':
            self.transport.write(
                'num_users is ' + str(self.factory.num_users) + '\r\n')
            self.transport.write('your name is ' + self.name + '\r\n')
            self.curFunc = self.handle_bye
        else:
            self.end('did not get status')

    def handle_bye(self, line):
        if line == 'bye':
            self.transport.write('bye ' + self.name + '\r\n')
            self.end('conversation ended')
        else:
            self.end('did not get bye')

    def connectionMade(self):
        print('connection made')
        self.transport.write('Welcome to MyServer\r\n')

    def lineReceived(self, line):
        print('got line ', line)
        self.curFunc(line)

    def connectionLost(self, reason=connectionDone):
        print('connection was lost')
        if self.loggedIn:
            self.factory.num_users -= 1


class MyFactory(Factory):
    protocol = MyProtocol

    def __init__(self):
        self.num_users = 0
        self.port = 8007


myFactory = MyFactory()
# pylint: disable=no-member
reactor.listenTCP(myFactory.port, myFactory)
reactor.run()
