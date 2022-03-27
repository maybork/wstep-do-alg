import math
from typing import Callable

import testsuite
from algorithms import bubblesort as bbl
from algorithms import insertionsort as ins
from algorithms import selectionsort as sel

tested_algs = (bbl.bubblesort, ins.insertionsort, sel.selectionsort)
lengths = (10, 100, 1000)


def performance_test(alg: Callable, n):
    t = round(testsuite.single_test(alg, n), 8)
    if t != 0:
        print(f"n = {n}: {t}, {round(n * math.log(n, 10) / t, 5)}")
    else:
        print(f"n = {n}: {t}, {round(n * math.log(n, 10) / 0.0001, 5)} "
              f"[t(n) was lower than the OS clock resolution, approximated it to 1µs]")


for alg in tested_algs:
    print(f"running tests for {alg.__name__}")
    for length in lengths:
        performance_test(alg, length)
