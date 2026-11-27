"""
Example for catching all exception types.

Note that "except Exception as e" DOES NOT catch "KeyboardInterrupt"
exception.

You can see that by uncommenting the line which raises "KeyboardInterrupt"...

If you want to catch all exceptions then use:
    except (Exception, KeyboardInterrupt) as exc:
"""

try:
    # raise KeyboardInterrupt()  # noqa: ERA001  teaching: kept in the comment for the reader
    raise ValueError("hello")
# this next line catches all exceptions, logs and throws them back...
except Exception as e:
    print("in except", e)
    raise
finally:
    print("finally is here")
