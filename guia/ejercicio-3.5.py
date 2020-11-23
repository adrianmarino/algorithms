#!/bin/python
import sys


def reserve(string):
    reserved_string = ''
    index = len(string) - 1
    while index >= 0:
        reserved_string += string[index]
        index -= 1
    return reserved_string


def is_palindrome(word):
    return word == reserve(word)


if __name__ == '__main__':
    word = sys.argv[1]
    print(f'=> "{word}" is{"" if is_palindrome(word) else " not a"} palindrome!')
