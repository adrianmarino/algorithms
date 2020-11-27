#!/bin/python


def multiply(numbers):
    return 1 if len(numbers) == 0 else numbers[0] * multiply(numbers[1:])


numbers = [2, 3, 4, 5]
print(f'multiply({numbers}) => {multiply(numbers)}')
