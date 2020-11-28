"""
Ejercicio 3

Dado una lista cuyos valores están entre 0 y 9, implementar un algoritmo que lo
ordena en O(|L|) Lineal.
"""


def sort(list):
    """
    Return ordered unrepeated elements.
    - Precondition: elements in (0, 9) range.
    - Order: O(n) Linear.
    """
    values_count = [False] * 9
    for e in list:
        values_count[e] = True

    i = 0
    result = []
    while i < len(values_count):
        if values_count[i]:
            result.append(i)
        i += 1

    return result


list_1 = list(range(1, 5))
list_1.reverse()
print(f'\nData: {list_1} - Result: {sort(list_1)}')
