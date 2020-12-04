#!/bin/python
"""
Programar una función recursiva es_par(n) que determine si un número n ∈ N es
par (i.e., que devuelva True si es par y False en caso contrario).
"""


def is_event(number):
    """
    Order: O(n)
    """
    if number == 0:
        return True
    elif number == 1:
        return False
    else:
        return is_event(number - 2)


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(True, is_event(0))
assert_equal(False, is_event(1))
assert_equal(True, is_event(2))
assert_equal(False, is_event(3))
assert_equal(True, is_event(4))
assert_equal(False, is_event(5))
