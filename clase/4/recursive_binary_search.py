#!/bin/python

def index_of(list, element):
    size = len(list)
    if size == 0:
        return -1
    return search(list, element, 0, size - 1)


def search(list, element, begin, end):
    if begin == end:
        return end
    else:
        mid = ((end - begin) // 2) + 1
        if element < list[mid]:
            return search(list, element, begin, mid - 1)
        else:
            return search(list, element, mid, end)


def assert_equal(expected, current, label='Result'):
    assert expected == current, f'{label}: expected -> {expected} != {current} <- current'


assert_equal(2, index_of(list(range(0, 10)), 2))
assert_equal(0, index_of([1, 2], 1))
assert_equal(1, index_of([1, 2], 2))
assert_equal(2, index_of([1, 2, 3], 3))
assert_equal(-1, index_of([], 3))
