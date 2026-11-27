"""
Solution
"""

import time
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

timing: dict[Any, Any] = {}


def time_it(func: Callable[..., Any]):
    def inner(*args: Any, **kwargs: Any):
        t_before = time.time()
        r = func(*args, **kwargs)
        t_after = time.time()
        t_func = t_after - t_before
        if func in timing:
            acc_time, n_calls = timing[func]
        else:
            acc_time = 0
            n_calls = 0
        acc_time += t_func
        n_calls += 1
        timing[func] = (acc_time, n_calls)
        return r
    return inner


def print_timing_summary() -> None:
    for k, v in timing.items():
        acc_time, n_calls = v
        print(f"function {k.__name__} took {acc_time / n_calls} to run on average")


@time_it
def add(a: int, b: int):
    return a + b


@time_it
def sub(a: int, b: int):
    return a - b


@time_it
def wait_1_sec() -> None:
    time.sleep(1)


print(f"did you know that 2+2={add(2,2)}")
print(f"did you know that 2-2={sub(2,2)}")
print("please wait while I call wait_1_sec")
wait_1_sec()

print_timing_summary()
