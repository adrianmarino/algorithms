#!/bin/python
import sys


def dividers(number_a):
    return [number_b for number_b in range(1, number_a) if not number_a % number_b]


def is_perfect(number):
    d = dividers(number)
    return number == sum(d)


if __name__ == '__main__':
    max_number = int(sys.argv[1])

    perfect_numbers = [str(number) for number in range(1, max_number + 1) if is_perfect(number)]

    print(f'Perfect number: {", ".join(perfect_numbers)}')
