"""
Ejercicio 2: Implementar en Python una función recursiva que sume todos los elementos de una lista.
"""


def sum(numbers):
    return 0 if len(numbers) == 0 else numbers[0] + sum(numbers[1:])


numbers = [1, 1, 2, 6, 6, 6, 3, 3]
print(f'sum: {sum(numbers)}')
