#!/bin/python
"""
Programar una función recursiva en Python cantidad_ocurrencias(n,l) que dada una lista de
enteros l y un número n, devuelva la cantidad de ocurrencias de n en l.
"""


def occurs(numbers, number):
    """
    Order: O(n)
    """
    if len(numbers) == 0:
        return 0
    else:
        return int(numbers[0] == number) + occurs(numbers[1:], number)


numbers = [2, 3, 4, 5, 3, 2, 10, 2]
number = 2
print(f'occurs({numbers}, {number}) => {occurs(numbers, number)}')
