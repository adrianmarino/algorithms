#!/bin/python
import sys


def reserve(string):
    """
    Order: O(n)
    """
    reserved_string = ''
    index = len(string) - 1
    while index >= 0:
        reserved_string += string[index]
        index -= 1
    return reserved_string


def is_palindrome1(word):
    """
    Order: O(n)
    """
    return word == reserve(word)


def is_palindrome2(word):
    """
    Order: O(n/2)
    """
    for i in range(len(word) // 2):
        left_char = word[i]
        right_char = word[-i - 1]
        if left_char != right_char:
            return False
    return True


word = sys.argv[1]
print(f'=> "{word}" is{"" if is_palindrome1(word) else " not a"} palindrome!')
print(f'=> "{word}" is{"" if is_palindrome2(word) else " not a"} palindrome!')
