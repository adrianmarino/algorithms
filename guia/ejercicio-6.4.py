#!/bin/python


def multiply(numbers):
    if len(numbers) == 0:
        return 1
    else:
        return numbers[0] * multiply(numbers[1:])


numbers = [2, 3, 4, 5]
print(f'multiply({numbers}) => {multiply(numbers)}')
