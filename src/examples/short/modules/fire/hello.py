"""
https://google.github.io/python-fire
"""

import fire


def hello(name: str = "World") -> str:
    return f"Hello {name}!"


if __name__ == "__main__":
    fire.Fire(hello)
