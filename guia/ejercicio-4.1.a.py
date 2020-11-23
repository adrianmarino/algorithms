#!/bin/python
import sys


def characters_count(words):
    count = 0
    for word in words:
        count += len(word)
    return count


if __name__ == '__main__':
    words = sys.argv[1:]
    print(f'"{" ".join(words)}" -> {characters_count(words)}')
