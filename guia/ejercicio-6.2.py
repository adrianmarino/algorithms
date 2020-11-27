#!/bin/python
import sys


def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


n = int(sys.argv[1])
print(f'fibonacci({n}) => {fibonacci(n)}')
