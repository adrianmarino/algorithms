#!/bin/python
def is_palindrome(word):
    """
    Order: O(n/2)
    """
    if len(word) == 0:
        return False
    i = 0
    last = len(word) - 1
    while i <= last // 2:
        # print(word, word[i], word[last - i])
        if word[i] != word[last - i]:
            return False
        i += 1
    return True


def assert_equal(expected, current):
    assert expected == current, f'expected -> {expected} != {current} <- current'


assert_equal(True, is_palindrome("1221"))
assert_equal(True, is_palindrome("12321"))
assert_equal(False, is_palindrome("1233456"))
assert_equal(False, is_palindrome("1234521"))
assert_equal(False, is_palindrome(""))
