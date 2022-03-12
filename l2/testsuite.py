import random
import time
from typing import Callable, Iterable
from collections import namedtuple


def single_test(length, alg):
    target = [random.randint(0, 100000) for _ in range(length)]
    start = time.time()
    alg(target)
    end = time.time()
    delta = end - start
    return delta


def run_tests(n: int, times: int, alg: Callable) -> tuple:
    """
    Tests a sorting algorithm multiple times and returns the average and maximum runtime

    Args:
        n (int):
        times (int): the amount of tests per test sample size
        alg (Callable): the tested algorithm

    Returns:
        tuple: the average and maximum runtime in seconds
    """
    temp = [single_test(n, alg) for i in range(times)]
    return (sum(temp) / len(temp), max(temp))
