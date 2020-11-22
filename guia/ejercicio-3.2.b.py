#!/bin/python
import sys


def fact(number):
    """
    Factorial recursive implementation.
    :param number: a number.
    :return: factorial.
    """
    if number == 1:
        return number
    else:
        return number * fact(number - 1)


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


if __name__ == '__main__':
    n = int(sys.argv[1])
    r = int(sys.argv[2])

    print(f'{n}C{r} => {nCr(n, r)}')
