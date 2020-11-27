#!/bin/python


def occurs(numbers, number):
    return int(numbers[0] == number) + occurs(numbers[1:], number) if len(numbers) else 0


numbers = [2, 3, 4, 5, 3, 2, 10, 2]
number = 2
print(f'occurs({numbers}, {number}) => {occurs(numbers, number)}')
