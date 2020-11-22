#!/bin/python
import sys

if __name__ == '__main__':
    number = int(sys.argv[1])

    sum = 0
    for i in range(1, number + 1):
        sum += 1 / i

    print(f'{number} sum is {sum}')
