#!/bin/python

def index_of(element, list):
    """
    Linear search: Search element index in a given list.
    - Order: O(n) (Linear).
    """
    index = 0
    while index < len(list):
        if list[index] == element:
            return index
        index += 1
    return -1


def all_under(element, list):
    """
    Returns all list elements that are less than element.
    - Order: O(n) (Linear).
    """
    return list[:index_of(element, numbers)]


numbers = list(range(1, 10))
element = 8

result = all_under(element, numbers)

print(f'{result} < {element}')
