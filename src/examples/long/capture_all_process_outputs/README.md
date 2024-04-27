This folder deals with the problem of capturing process output.
Doing so only for stdout and stderr is not that difficult.
But it seems that redirecting ttys is harder.

I all comes down to openpty(3) and a similar implementation in python.

See the code for the details.
