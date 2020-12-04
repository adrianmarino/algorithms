#!/bin/python

def power_of(number, power):
    """
    Order: O(power)
    """
    if power == 0:
        return 1
    else:
        return number * power_of(number, power - 1)


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(9, power_of(3, 2))
assert_equal(8, power_of(2, 3))
assert_equal(1, power_of(2, 0))
