"""
This is an example of how to read comments from a yaml file.

References:
- https://stackoverflow.com/questions/7255885/save-dump-a-yaml-file-with-comments-in-pyyaml
"""

from typing import TYPE_CHECKING, Any

import ruamel.yaml
from ruamel.yaml.comments import CommentedMap, CommentedSeq

if TYPE_CHECKING:
    from ruamel.yaml.tokens import CommentToken


def get_comments_map(self: Any, key: str):
    coms: list[CommentToken] = []
    comments = self.ca.items.get(key)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        if isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms


def get_comments_seq(self: Any, idx: int):
    coms: list[CommentToken] = []
    comments = self.ca.items.get(idx)
    if comments is None:
        return coms
    for token in comments:
        if token is None:
            continue
        if isinstance(token, list):
            coms.extend(token)
        else:
            coms.append(token)
    return coms


def yield_comments(data: Any):
    if isinstance(data, CommentedMap):
        if isinstance(data.ca.comment, list) and isinstance(data.ca.comment[1], list):
            yield "", data.ca.comment[1][0].value.rstrip()
        for k, v in data.items():
            for comment in get_comments_map(data, k):
                for frag in comment.value.split("\n"):
                    if frag == "":
                        continue
                    yield k, frag.rstrip()
            yield from yield_comments(v)
    elif isinstance(data, CommentedSeq):
        if isinstance(data.ca.comment, list) and isinstance(data.ca.comment[1], list):
            yield "", data.ca.comment[1][0].value.rstrip()
        for idx, item in enumerate(data):
            for comment in get_comments_seq(data, idx):
                for frag in comment.value.split("\n"):
                    if frag == "":
                        continue
                    yield idx, frag.rstrip()
            yield from yield_comments(item)


def main() -> None:
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
            for _, y in yield_comments(data):
                # print(f"[{y}]")  # noqa: ERA001  teaching: kept in the comment for the reader
                to_add = y.split("#")[1]
                my_sum += int(to_add)
            print(my_sum)


main()
