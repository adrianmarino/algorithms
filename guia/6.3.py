#!/bin/python
"""
Programar una función recursiva es_par(n) que determine si un número n ∈ N es
par (i.e., que devuelva True si es par y False en caso contrario).
"""
import sys


def is_even(number):
    if number <= 1:
        return not number
    else:
        return is_even(number - 2)


number = int(sys.argv[1])
print(f'{number} is {"even" if is_even(number) else "odd"}')
