#!/bin/python


def sum(numbers):
    """
    Returns numbers sum.
    Order: O(n)
    """
    result = 0
    index = 0
    while index < len(numbers):
        result += numbers[index]
        index += 1
    return result


def mean(numbers):
    """
    Returns numbers mean.
    Order: O(n)
    """
    return sum(numbers) / len(numbers)


numbers = list(range(1, 131))
print(f'mean[{numbers[0]}...{numbers[-1]}] => {mean(numbers)}')
