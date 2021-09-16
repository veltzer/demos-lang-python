"""
A basic example of yaml dump
"""

import yaml

d = {"foo": "bar"}

with open('/tmp/out.yaml', 'w') as f:
    yaml.safe_dump(d, f)
