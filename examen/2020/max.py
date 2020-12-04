#!/bin/python


def max(list):
    """
    Order: O(n)
    """
    if len(list) == 1:
        return list[0]
    else:
        tail_max = max(list[1:])
        return list[0] if list[0] > tail_max else tail_max


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(3, max([3, 2, 1]))
assert_equal(800, max([10, 100, 800]))
assert_equal(1, max([1]))
