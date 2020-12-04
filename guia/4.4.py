#!/bin/python
import math
import sys


def min(numbers):
    """
    Order: O(n)
    """
    min_num = math.inf
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def max(numbers):
    """
    Order: O(n)
    """
    max_num = -math.inf
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def sum(numbers):
    """
    Order: O(n)
    """
    result = 0
    for num in numbers:
        result += num
    return result


def mean(numbers):
    """
    Order: O(n)
    """
    return sum(numbers) / len(numbers)


def str_list_to_int_list(list):
    return [int(element) for element in list]


if __name__ == '__main__':
    str_numbers = sys.argv[1:]
    numbers = str_list_to_int_list(sys.argv[1:])

    print(f'Numbers: {", ".join(str_numbers)}')
    print(f'Min: {min(numbers)}')
    print(f'Max: {max(numbers)}')
    print(f'mean: {mean(numbers)}')
