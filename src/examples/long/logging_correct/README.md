# Correct Logging

This example shows that you should not do

```python
logger = logging.getLogger(__name__)
```

outside of any function since it will break if the main
logging module is configured with:

```config
disable_existing_loggers: True
```

which, by the way, it should as this is the right configuration.

References:
- [link](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
