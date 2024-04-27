# Standard config file for python logging

This is an example of a large project using the python logging framework.

These are the things to remember:
Sub loggers determine which messages will be logged but still pass
on the messaged to their parents (and onto root). This means that
* you usually don't need handles for sub loggers (let root do
the printing for you).
* if you want to print differently for a sub logger add your own
handler.
* if you don't want to propagate to root put "propagate=0".
