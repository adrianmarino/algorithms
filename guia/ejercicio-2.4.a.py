#!/bin/python
import sys


def factorial(number):
    """
    Factorial recursive implementation.
    :param number: a number.
    :return: factorial.
    """
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(sys.argv[1])
    print(f'{number}! is {factorial(number)}')
