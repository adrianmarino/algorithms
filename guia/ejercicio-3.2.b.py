#!/bin/python
import sys


def fact(num):
    """
    Order: O(n)
    """
    return 1 if num == 0 else num * fact(num - 1)


def nCr(n, r):
    """
    Order: O(n + r + (n-r)) => O(n)
    """
    return fact(n) / (fact(r) * fact(n - r))


if __name__ == '__main__':
    n = int(sys.argv[1])
    r = int(sys.argv[2])

    print(f'{n}C{r} => {nCr(n, r):.0f}')
