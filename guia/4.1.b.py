#!/bin/python
import sys

words = sys.argv[1:]
print(f'"{" ".join(words)}" -> {sum([len(w) for w in words])}')
