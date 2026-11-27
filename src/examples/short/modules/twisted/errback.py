"""
An example of using errbacks in twisted.
"""

from twisted.internet import reactor
from twisted.web.client import Agent

# from twisted.protocols.basic import LineReceiver  # noqa: ERA001  teaching: kept in the comment for the reader


def my_other_callback(content):
    print(f"in other_callback {content}")
    reactor.stop()


def my_callback(response):
    print(f"in callback {response}")


def my_errback(error):
    print("in error", error)
    reactor.stop()


def main():
    agent = Agent(reactor)

    deferred = agent.request(
        uri="http://localhost",
        method="GET",
    )
    deferred.addCallback(my_callback)
    deferred.addErrback(my_errback)
    reactor.run()


if __name__ == "__main__":
    main()
