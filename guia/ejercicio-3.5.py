#!/bin/python
import sys


def reserve(string):
    reserved_string = ''
    index = len(string) - 1
    while index >= 0:
        reserved_string += string[index]
        index -= 1
    return reserved_string


def is_palindrome1(word):
    return word == reserve(word)


def is_palindrome2(word):
    for i in range(0, len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


word = sys.argv[1]
print(f'=> "{word}" is{"" if is_palindrome1(word) else " not a"} palindrome!')
print(f'=> "{word}" is{"" if is_palindrome2(word) else " not a"} palindrome!')
