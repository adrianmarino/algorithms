#!/bin/python
import sys


def characters_count(words):
    count = 0
    for word in words:
        count += len(word)
    return count


words = sys.argv[1:]
count = characters_count(words)

print(f'{" ".join(words)} -> {count}')
