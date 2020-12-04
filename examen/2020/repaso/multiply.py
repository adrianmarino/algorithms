#!/bin/python


def multiply(a, b):
    """
    Si a < b => O(b)
    Si a > b => O(a)
    """
    if a < b:
        return multiply_aux(a, b)
    else:
        return multiply_aux(b, a)


def multiply_aux(a, b):
    """
    Order: O(b)
    """
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(20, multiply(10, 2))
assert_equal(60, multiply(2, 30))
assert_equal(0, multiply(2, 0))
