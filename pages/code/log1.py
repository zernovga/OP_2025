from io import TextIOWrapper
from math import sqrt
from random import randint
from typing import Tuple


def quadratic_equation(a: int, b: int, c: int, logfile: TextIOWrapper) -> Tuple[float]:
    def qa(text: str):
        return f"quadratic_equation:\t{text}\n"

    d = b**2 - 4 * a * c
    logfile.write(qa("a: {0}, b: {1}, c: {2}".format(a, b, c)))
    try:
        sq = sqrt(d)
    except Exception as exc:
        logfile.write(qa("Exception: {0}".format(str(exc))))
    else:
        logfile.write(qa("Discriminant square root: {0}".format(sq)))
        x1 = -b + sq / (2 * a)
        x2 = -b - sq / (2 * a)
        logfile.write(qa("x1: {0}, x2: {1}".format(x1, x2)))

        return x1, x2


def rnd(a: int = -10, b: int = 10) -> int:
    return randint(a, b)


equations = [(rnd(), rnd(), rnd()) for _ in range(10)]

if __name__ == "__main__":
    with open("lections/slides/log.txt", "at") as logfile:
        for values in equations:
            print("Values\t a: {0}, b: {1}, c: {2}".format(*values))
            print(
                "Result\t x1: {0}, x2: {1}".format(
                    *quadratic_equation(*values, logfile)
                )
            )
