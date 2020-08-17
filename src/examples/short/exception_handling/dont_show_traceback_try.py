"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

References:
- http://stackoverflow.com/questions/17784849/in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""


def do_error():
    try:
        raise ValueError('core')
    except Exception as e:
        raise ValueError('outer') from e


def main():
    try:
        do_error()
    except (Exception, KeyboardInterrupt) as e:
        while e.__cause__:
            e = e.__cause__
        print(e)

main()
