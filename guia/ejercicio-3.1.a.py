#!/bin/python
import sys


def multiply(a, b):
    return sum([a for _ in range(0, b)])


if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(f'{a} * {b} => {multiply(a, b)}')
