#!/bin/python
"""
Programar una función recursiva es_par(n) que determine si un número n ∈ N es
par (i.e., que devuelva True si es par y False en caso contrario).
"""
import sys


def is_event(number):
    return not number if number <= 1 else is_event(number - 2)


number = int(sys.argv[1])
print(f'{number} is {"event" if is_event(number) else "odd"}')
