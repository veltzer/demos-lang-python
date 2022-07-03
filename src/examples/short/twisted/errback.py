"""
An example of using errbacks in twisted.
"""

from twisted.internet import reactor
from twisted.web.client import Agent


# from twisted.protocols.basic import LineReceiver


def my_other_callback(content):
    print(f"in other_callback {content}")
    # pylint: disable=no-member
    reactor.stop()


def my_callback(response):
    print(f"in callback {response}")


def my_errback(error):
    print('in error', error)
    # pylint: disable=no-member
    reactor.stop()


def main():
    agent = Agent(reactor)

    deferred = agent.request(
        uri='http://localhost',
        method='GET',
    )
    deferred.addCallback(my_callback)
    deferred.addErrback(my_errback)
    # pylint: disable=no-member
    reactor.run()  # type: ignore


if __name__ == '__main__':
    main()
