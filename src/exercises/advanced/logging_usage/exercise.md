# Logging Usage

Use the python logging library.

Create two logging object.
The first logger object:
* will write to a file called "/tmp/log.txt"
* will have severity "WARNING" (this means it will only print message of severity WARNING and above)

The second logger object:
* will only send all of his messages to the system logger.
    (Eventlog in windows, syslog in Linux/MacOSX).
    So it shouldn't log to the screen
* will have severity "DEBUG"

Demonstrate that your loggers work as expected.
