"""
Ejercicio 2:

Implementar en Python una función que dadas dos listas ordenadas L1 y L2 sin
elementos repetidos devuelva la cantidad de elementos de L1 que aparecen en
L2 con orden O(|L1| + |L2|).

def enAmbasListas(l1, l2): # l1 y l2 están ordenadas y sin repetidos
"""


def index_of(element, list):
    """
    Binary search: Search element index in a given list.
    - Precondition: list must be sorted ascending.
    - Order: O(log(n)) < O(n)
    """
    size = len(list)
    if size == 0:
        return -1

    left, right = 0, size - 1
    while left < right:
        index = (left + right) // 2
        if list[index] < element:
            left = index + 1
        else:
            right = index

    return left if list[left] == element else -1


def intersection1(list_a, list_b):
    """
    Description: Get commons elements.
    Order: O(n^2) Quadratic
    """
    if list_a == list_b:
        return list_a

    commons = []
    for a in list_a:
        for b in list_b:
            if a == b:
                commons.append(b)

    return commons


def intersection2(list_a, list_b):
    """
    Description: Get commons elements.
    Order: O(n) Linear
    """
    if list_a == list_b:
        return list_a

    index = {i: a for i, a in enumerate(list_a)}
    return [b for b in list_b if b in index]


def intersection3(list_a, list_b):
    """
    Description: Get commons elements.
    Precondition: Both lists are ordered (asc) and has not repeats.
    Order: O(n log(n))
    """
    if list_a == list_b:
        return list_a

    return [a for a in list_a if index_of(a, list_b) > -1]


list_a, list_b = list(range(1, 20)), list(range(1, 10))
print(f'\nData:\n-List A: {list_a}\n-List B: {list_b}\n')

print('Implementations:')
print(f'- Using a hash-table O(n) -> {intersection2(list_a, list_b)}')
print(f'- Using BinarySearch O(n log(n)) -> {intersection3(list_a, list_b)}')
print(f'- Using for-for-if O(n^2) -> {intersection1(list_a, list_b)}')
