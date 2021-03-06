#!/bin/python

def is_prime(number):
    """
    Order: O(n^0.5)
    """
    if number == 1:
        return False

    i = 2
    it = int(number ** 0.5)
    while i <= it and number % i != 0:
        i += 1
    return i == it + 1


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


# Primes: 2, 3, 5, 7, 11, 13, 17
assert_equal(False, is_prime(1))
assert_equal(True, is_prime(2))
assert_equal(True, is_prime(3))
assert_equal(False, is_prime(4))
assert_equal(True, is_prime(5))
assert_equal(False, is_prime(6))
assert_equal(True, is_prime(7))
assert_equal(False, is_prime(8))
