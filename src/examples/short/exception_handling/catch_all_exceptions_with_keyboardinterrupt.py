"""
Example for catching all exception types.

Note that "except Exception as e" DOES NOT catch "KeyboardInterrupt"
exception.

You can see that by hitting CTRL+C while this is running.

If you want to catch all exceptions then use:
    except (Exception, KeyboardInterrupt) as exc:
"""

try:
    raise KeyboardInterrupt()
# this next line catches all exceptions, logs and throws them back...
except (Exception, KeyboardInterrupt) as e:
    print("in except", e)
    raise e
finally:
    print("finally is here")
