#!/bin/python
import unittest


def index_of(element, list):
    """
    Binary search: Search element index in a given list.
    - Precondition: list must be sorted ascending.
    - Order: O(log(n)) < O(n)
    """
    size = len(list)
    if size == 0:
        return -1

    left, right = 0, size - 1
    while left < right:
        index = (left + right) // 2
        if list[index] < element:
            left = index + 1
        else:
            right = index

    return left if list[left] == element else -1


class BinarySearchTest(unittest.TestCase):
    def test_when_has_an_ordered_list_and_search_a_contained_element_it_returns_searched_element_index(self):
        # Prepare
        numbers = list(range(1, 10))

        # Perform
        index = index_of(element=9, list=numbers)

        # Asserts
        self.assertEqual(8, index)

    def test_when_has_an_ordered_list_and_search_non_contained_element_it_that_not_return_any_index(self):
        # Prepare
        numbers = list(range(1, 10))

        # Perform
        index = index_of(element=100, list=numbers)

        # Asserts
        self.assertEqual(-1, index)

    def test_when_search_over_an_empty_list_it_always_return_any_index(self):
        # Prepare
        numbers = list()

        # Perform
        index = index_of(element=100, list=numbers)

        # Asserts
        self.assertEqual(-1, index)


if __name__ == '__main__':
    unittest.main(verbosity=2)
