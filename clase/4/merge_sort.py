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
    return merge_sort_(list, 0, len(list))


def merge_sort_(list, low, high):
    if low < high:
        mid = low + (high - low) // 2
        list1 = merge_sort_(list, low, mid)
        list2 = merge_sort_(list, mid + 1, high)
        return merge(list1, list2)
    else:
        return list[low:high + 1]


numbers = list(range(1, 27))
random.shuffle(numbers)
print('Input: ', numbers)
print('Output: ', merge_sort(numbers))
