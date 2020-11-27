#!/bin/python

def index_of(element, list):
    """
    Binary search: Search element index in a given list.
    - Precondition: list must be sorted ascending.
    - Order: O(log(n)) < O(n)
    """
    size = len(list)
    if size == 0:
        return -1

    left, right = 0, size - 1
    while left < right:
        index = (left + right) // 2
        if list[index] < element:
            left = index + 1
        else:
            right = index

    return left if list[left] == element else -1


def all_under(element, list):
    """
    Returns all list elements that are less than.
    - Order: O(log(n))
    """
    return list[:index_of(element, numbers)]


numbers = list(range(1, 10))
element = 8

result = all_under(element, numbers)

print(f'{result} < {element}')
