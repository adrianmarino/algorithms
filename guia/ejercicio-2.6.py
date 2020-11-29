#!/bin/python
import sys


def dividers(number_a):
    result = []
    for number_b in range(1, number_a):
        if not number_a % number_b:
            result.append(number_b)
    return result


def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


def is_perfect(number):
    return number == sum(dividers(number))


if __name__ == '__main__':
    max_number = int(sys.argv[1])

    perfect_numbers = [str(number) for number in range(1, max_number + 1) if is_perfect(number)]

    print(f'Perfect number: {", ".join(perfect_numbers)}')
