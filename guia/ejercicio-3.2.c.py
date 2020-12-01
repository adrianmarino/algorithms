#!/bin/python
import sys


def fact(num):
    """
    Order: O(n)
    """
    return num if num == 1 else num * fact(num - 1)


def nCr(n, r):
    """
    Order: O(n + r + (n -r))
    """
    return fact(n) / (fact(r) * fact(n - r))


if __name__ == '__main__':
    n = int(sys.argv[1])

    for i in range(1, n):
        print(f'{n}C{i} => {nCr(n, i)}')
