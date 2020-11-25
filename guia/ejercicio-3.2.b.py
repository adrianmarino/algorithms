#!/bin/python
import sys


def fact(num):
    return num if num == 1 else num * fact(num - 1)


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


if __name__ == '__main__':
    n = int(sys.argv[1])
    r = int(sys.argv[2])

    print(f'{n}C{r} => {nCr(n, r):.0f}')
