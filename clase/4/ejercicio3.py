#!/bin/python
"""
Ejercicio 3: Implementar una función que, usando Divide & Conquer, encuentre el máximo de
             una lista de enteros positivos:

             def maximo(l):
"""


def max(list):
    if len(list) == 0:
        return 0
    else:
        head = list[0]
        max_tail = max(list[1:])
        return head if head > max_tail else max_tail


print(max([10, 1, 2, 6, 6, 3, 3]) == 10)
print(max([2, 3]) == 3)
print(max([3]) == 3)
print(max([]) == 0)
