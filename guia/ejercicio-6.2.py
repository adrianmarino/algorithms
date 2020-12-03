#!/bin/python
"""
La sucesión de Fibonacci es una secuencia de números en la cual los dos primeros términos
son 1 y los siguientes se definen como la suma de los dos anteriores. A continuación, se
observan los primeros diez términos de la sucesión:

            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, . . .

Programar una función recursiva en Python fibonac
"""


def fibonacci(n):
    # Son dos casos base:
    # - Si se achica en 1, termina siendo 0.
    # - Si se achica en 2, termina siendo 1 .
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1) == 1)
print(fibonacci(2) == 1)
print(fibonacci(3) == 2)
print(fibonacci(4) == 3)
print(fibonacci(5) == 5)
print(fibonacci(6) == 8)
print(fibonacci(7) == 13)
print(fibonacci(8) == 21)
print(fibonacci(9) == 34)
print(fibonacci(10) == 55)
