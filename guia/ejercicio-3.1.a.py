#!/bin/python
import sys


def sum(numbers):
    result = 0
    i = 0

    while i < len(numbers):
        result = result + numbers[i]
        i = i + 1

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


a, b = int(sys.argv[1]), int(sys.argv[2])
print(f'{a} * {b} => {multiply(a, b)}')
