#!/bin/python
import sys


def multiply(a, b):
    return sum([a for _ in range(0, b)])


def pow(number, pot):
    result = number
    for _ in range(0, pot - 1):
        result = multiply(result, number)
        print(result)
    return result


if __name__ == '__main__':
    number = int(sys.argv[1])
    pot = int(sys.argv[2])

    print(f'{number} ^ {pot} => {pow(number, pot)}')
