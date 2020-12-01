#!/bin/python
import sys


def repeat(times, char):
    """
    Order: O(n)
    """
    output = ''
    i = 0
    while i < times:
        output += char
        i += 1
    return output


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(repeat(n, '*'))
