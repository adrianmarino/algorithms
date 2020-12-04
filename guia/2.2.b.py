#!/bin/python
import sys

if __name__ == '__main__':
    n = int(sys.argv[1])

    odd_numbers = [str(number) for number in range(1, n + 1) if number % 2]

    print(', '.join(odd_numbers))
