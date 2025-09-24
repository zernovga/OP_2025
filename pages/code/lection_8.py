import pdb
from math import sqrt
from random import randint
from typing import Tuple


def quadratic_equation(a: int, b: int, c: int) -> Tuple[float]:
    d = b**2 - 4 * a * c
    sq = sqrt(d)
    x1 = -b + sq / (2 * a)
    x2 = -b - sq / (2 * a)

    return x1, x2


def rnd(a: int = -10, b: int = 10) -> int:
    return randint(a, b)


equations = [(rnd(), rnd(), rnd()) for _ in range(10)]

if __name__ == "__main__":
    pdb.set_trace()
    for values in equations:
        print("Values\t a: {0}, b: {1}, c: {2}".format(*values))
        print("Result\t x1: {0}, x2: {1}".format(*quadratic_equation(*values)))
