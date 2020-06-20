#!/usr/bin/env python

"""
A basic example of loading YAML
Make sure you use the "safe_load" method and not the "load" method
that will give you warnings.

References:
- https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
"""

import yaml

with open("data_samples/basic.yaml", 'r') as stream:
    try:
        data=yaml.safe_load(stream)
        assert "concepts" in data
    except yaml.YAMLError as exc:
        print(exc)
