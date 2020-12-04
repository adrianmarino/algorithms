#!/bin/python
"""
Ejercicio 3

Dado una lista cuyos valores están entre 0 y 9, implementar un algoritmo que lo
ordena en O(|L|) Lineal.
"""


def numbers_index(numbers):
    """
    Retorna una lista de 0..9 elementos cada uno un boolean
    que es True cuando el indice existe en numbers.

    - Orden: O(n).
    """
    number_index = [False] * 9
    i = 0
    while i < len(numbers):  # Itera n.
        number_index[numbers[i]] = True
        i += 1
    return number_index


def sort(numbers):
    """
    Ordena numbers ascendentemente.

    - Precondiciones: Solo numeros del 0 al 9.
    - Orden: O(n).
    """
    index = numbers_index(numbers)

    i = 0
    sorted_numbers = []
    while i < len(index):  # Itera del 0 al 9.
        if index[i]:
            sorted_numbers.append(i)
        i += 1

    return sorted_numbers


numbers = list(range(1, 5))
numbers.reverse()
print(f'\nInput: {numbers} -> Sorted: {sort(numbers)}')
