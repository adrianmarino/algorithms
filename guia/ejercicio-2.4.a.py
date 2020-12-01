#!/bin/python
import sys


def fact(number):
    """
    Factorial recursive implementation.
    Order: O(n)
    :param number: a number.
    :return: factorial.
    """
    if number == 1:
        return number
    else:
        return number * fact(number - 1)


if __name__ == '__main__':
    number = int(sys.argv[1])
    print(f'{number}! is {fact(number)}')
