#!/bin/python
import random


def merge(list1, list2):
    """
    Description: Perform a lists union.
    - Precondition: both list must be sorted ascending.
    - Order: O(n).
    """
    result = []

    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1

    if i == len(list1):
        result.extend(list2[j:])

    if j == len(list2):
        result.extend(list1[i:])

    return result


def merge_sort(list):
    """
    Description: Sort the list in ascending order.
    - Order: O(n * log(n))
    """
    if len(list) == 1:
        return list

    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


numbers = list(range(1, 11))
random.shuffle(numbers)
print('Input:', numbers)
print('Output:', merge_sort(numbers))
