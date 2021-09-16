"""
This is an example of how to read comments from a yaml file.

References:
- https://stackoverflow.com/questions/7255885/save-dump-a-yaml-file-with-comments-in-pyyaml
"""

import ruamel.yaml

with open("data/yaml/comments.yaml", "r") as stream:
    yaml = ruamel.yaml.YAML()
    data = yaml.load(stream)
    print(dir(data))
