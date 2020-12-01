#!/bin/python
"""
Programar una función recursiva en Python productoria(l) que dada una lista no vacía de
enteros l devuelva el resultado de multiplicar todos los números de l.
"""


def multiply(numbers):
    """
    Order: O(n)
    """
    if len(numbers) == 0:
        return 1
    else:
        return numbers[0] * multiply(numbers[1:])


numbers = [2, 3, 4, 5]
print(f'multiply({numbers}) => {multiply(numbers)}')
