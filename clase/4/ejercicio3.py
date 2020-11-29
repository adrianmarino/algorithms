#!/bin/python
"""
Ejercicio 3: Implementar una función en Python que, usando Divide & Conquer, encuentre el máximo de
             una lista de enteros positivos:

             def maximo(l):
"""


def max(numbers):
    if len(numbers) == 0:
        return 0
    else:
        num = numbers[0]
        sub_max = max(numbers[1:])
        return num if num > sub_max else sub_max


numbers = [10, 1, 1, 2, 6, 6, 6, 3, 3]
print(f'List: {numbers} ->  Max: {max(numbers)}')
