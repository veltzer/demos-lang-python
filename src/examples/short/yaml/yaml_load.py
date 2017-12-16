#!/usr/bin/env python

"""
A basic example of loading YAML

References:
- https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
"""

import yaml

with open("data_samples/basic.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
