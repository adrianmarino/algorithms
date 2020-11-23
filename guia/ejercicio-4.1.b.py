#!/bin/python
import sys


def characters_count(words):
    return sum([len(w) for w in words])
1

if __name__ == '__main__':
    words = sys.argv[1:]
    print(f'"{" ".join(words)}" -> {characters_count(words)}')
