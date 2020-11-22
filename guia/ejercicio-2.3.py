#!/bin/python
import sys

if __name__ == '__main__':
    rows_number = int(sys.argv[1])

    for r in range(1, rows_number + 1):
        [print('*', end=' ') for _ in range(1, r + 1)]
        print()
