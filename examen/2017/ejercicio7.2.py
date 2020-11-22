#!/bin/python
import unittest


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def input_validation(elements):
    if len(elements) == 0:
        raise Exception("Empty list!")

    if not type(elements) is list:
        raise Exception("can only be applied to ordered lists!")


def more_frequently_element(elements):
    """
    Returns more more frequently element along with its frequency.

    Precondition: 'elements' is an ascending ordered numeric list.

    Example:

    elements  =  [1, 2, 4, 4]

    -------------------
    i  Max  curr, next
    -------------------
    0  1    1     2
    1  1    2     4
    2  1    4     4
    3  2    4     None
    -------------------

    """
    input_validation(elements)

    more_freq_element = None
    max_frequency = count = i = 0

    while i < len(elements):
        current_element = elements[i]
        next_element = elements[i + 1] if i + 1 < len(elements) else None
        i += 1

        count += 1

        if next_element != current_element:
            if count > max_frequency:
                max_frequency = count
                more_freq_element = current_element
            count = 0

    return more_freq_element, max_frequency


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
class MoreFrequentlyElementFncTestCases(unittest.TestCase):
    def when_give_an_ordered_list_arg_it_return_more_frequently_element_with_your_frequency(self):
        # Prepare
        fn_argument = [1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7, 4, 4, 4, 4]

        # Perform
        element, frequency = more_frequently_element(fn_argument)

        # Asserts
        self.assertEqual(6, element)
        self.assertEqual(4, frequency)

    def when_give_an_empty_list_arg_it_cant_perform_algorithm_and_raise_an_exception(self):
        # Prepare
        fn_argument = []

        # Perform & assert
        with self.assertRaises(Exception):
            more_frequently_element(fn_argument)

    def when_give_an_non_list_arg_perform_algorithm_and_raise_an_exception(self):
        # Prepare
        fn_argument = 123

        # Perform & assert
        with self.assertRaises(Exception):
            more_frequently_element(fn_argument)


if __name__ == '__main__':
    unittest.main()
