#!/bin/python
import sys


def sum(numbers):
    result = 0
    i = 0

    while i < len(numbers):
        result += numbers[i]
        i += 1

    return result


def repeat(number, times):
    result = []
    i = 0

    while i < times:
        result.append(number)
        i += 1

    return result


def multiply(a, b):
    return sum(repeat(a, b))


def pow(number, pot):
    result = number
    i = 0

    while i < (pot - 1):
        result = multiply(result, number)
        i += 1

    return result


if __name__ == '__main__':
    number = int(sys.argv[1])
    pot = int(sys.argv[2])

    print(f'{number} ^ {pot} => {pow(number, pot)}')
