#!/bin/python
"""
La sucesión de Fibonacci es una secuencia de números en la cual los dos primeros términos
son 1 y los siguientes se definen como la suma de los dos anteriores. A continuación, se
observan los primeros diez términos de la sucesión:

            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, . . .

Programar una función recursiva en Python fibonac
"""
import sys


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(sys.argv[1])
print(f'fibonacci({n}) => {fibonacci(n)}')
