#!/bin/python

def multiply(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    else:
        return list[0] * multiply(list[1:])


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(4, multiply([2, 2]))
assert_equal(6, multiply([1, 2, 3]))
assert_equal(5, multiply([5]))
assert_equal(0, multiply([]))
