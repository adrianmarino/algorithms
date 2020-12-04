#!/bin/python


def occurs(list, element):
    """
    Order: O(n)
    """
    if len(list) == 0:
        return 0
    else:
        return int(element == list[0]) + occurs(list[1:], element)


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(2, occurs([1, 2, 2, 3, 3, 4, 5], 2))
assert_equal(1, occurs([1, 2, 2, 3, 3, 4, 5], 5))
assert_equal(1, occurs([1, 2, 2, 3, 3, 4, 5], 1))
assert_equal(2, occurs([1, 2, 2, 3, 3, 4, 5], 3))
assert_equal(0, occurs([1, 2, 2, 3, 3, 4, 5], 100))
assert_equal(1, occurs([1], 1))
assert_equal(0, occurs([], 1))
