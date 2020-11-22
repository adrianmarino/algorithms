#!/bin/python
import sys


def line(times, char='*'):
    output = ''
    for _ in range(0, times):
        output += char
    return output


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(line(n))
