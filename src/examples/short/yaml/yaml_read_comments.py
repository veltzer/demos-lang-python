"""
This is an example of how to read comments from a yaml file.

References:
- https://stackoverflow.com/questions/7255885/save-dump-a-yaml-file-with-comments-in-pyyaml
"""

import ruamel.yaml
from ruamel.yaml.comments import CommentedMap, CommentedSeq, Comment


def get_comments_map(self, key):
    coms = []
    comments = self.ca.items.get(key)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        elif isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms


def get_comments_seq(self, idx):
    coms = []
    comments = self.ca.items.get(idx)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        elif isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms


def walk_data(data):
    if isinstance(data, CommentedMap):
        if isinstance(data.ca.comment, list):
            if isinstance(data.ca.comment[1], list):
                yield "", data.ca.comment[1][0].value.rstrip()
        for k, v in data.items():
            for comment in get_comments_map(data, k):
                yield k, comment.value.rstrip()
            yield from walk_data(v)
    elif isinstance(data, CommentedSeq):
        if isinstance(data.ca.comment, list):
            if isinstance(data.ca.comment[1], list):
                yield "", data.ca.comment[1][0].value.rstrip()
        for idx, item in enumerate(data):
            for comment in get_comments_seq(data, idx):
                yield k, comment.value.rstrip()
            yield from walk_data(item)

filenames = [
        "data/yaml/comments1.yaml",
        "data/yaml/comments2.yaml",
        "data/yaml/comments3.yaml",
]
for filename in filenames: 
    with open(filename) as stream:
        print(f"{filename}...", end="")
        yaml = ruamel.yaml.YAML()
        data = yaml.load(stream)
        my_sum = 0
        for _, y in walk_data(data):
            for frag in y.split("\n"):
                to_add = frag.split("#")[1]
                my_sum += int(to_add) 
        print(my_sum)
