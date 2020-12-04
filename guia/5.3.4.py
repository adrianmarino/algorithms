#!/bin/python
"""
Dado un n natural, obtener su representación binaria (como una lista de 1s y 0s). 

O(log(n))
"""
import sys


def to_binary(num):
    """
    Order: O(log(n))
    """
    if num > 1:
        return to_binary(num // 2) + [num % 2]
    else:
        return [num % 2]


natural = int(sys.argv[1])
print(f'Natural: {natural} --> Binary: {to_binary(natural)}')
