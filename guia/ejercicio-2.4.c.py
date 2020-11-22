#!/bin/python
import sys

if __name__ == '__main__':
    number = int(sys.argv[1])
    print(f'{number} sum is {sum(list(range(1, number + 1)))}')
