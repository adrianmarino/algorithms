#!/bin/python

def index_of(list, element):
    size = len(list)
    return -1 if size == 0 else search(list, element, 0, size - 1)


def search(list, element, begin, end):
    if begin == end:
        return end if element == list[end] else -1
    else:
        mid = ((end - begin) // 2) + 1
        if element < list[mid]:
            return search(list, element, begin, mid - 1)
        else:
            return search(list, element, mid, end)


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(2, index_of(list(range(0, 10)), 2))
assert_equal(2, index_of([1, 2, 3], 3))

assert_equal(0, index_of([1, 2], 1))
assert_equal(1, index_of([1, 2], 2))

assert_equal(-1, index_of([1, 2, 3], 1000))
assert_equal(-1, index_of([], 3))
