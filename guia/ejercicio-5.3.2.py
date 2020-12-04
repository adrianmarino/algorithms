#!/bin/python
"""
Calcular la mediana de una lista de enteros en orden O(n^2).
"""


def swap(list, i, j):
    value = list[i]
    list[i] = list[j]
    list[j] = value


def bubble_sort(elements):
    """
    Returns numbers sum.
    - Order: O(n^2)
    """
    sorted = list(elements)
    i = 0
    while i < len(sorted):
        j = 0
        while j < len(sorted) - 1:
            if sorted[j] > sorted[j + 1]:
                swap(sorted, j, j + 1)
            j += 1
        i += 1
    return sorted


def even_number(number):
    return number % 2 == 0


def median(numbers):
    """
    Returns numbers median.
    - Order: O(n^2)
    """
    sorted = bubble_sort(numbers)
    size = len(sorted)
    mid = (size // 2)
    if even_number(size):
        return (sorted[mid - 1] + sorted[mid]) / 2
    else:
        return sorted[mid]


numbers = list(range(1, 10))[::-1]
ordered_numbers = bubble_sort(numbers)
print(f'sort => {ordered_numbers}')
print(f'median{ordered_numbers} => {median(numbers)}')

numbers = list(range(1, 9))[::-1]
ordered_numbers = bubble_sort(numbers)
print(f'sort => {ordered_numbers}')
print(f'median{ordered_numbers} => {median(numbers)}')
