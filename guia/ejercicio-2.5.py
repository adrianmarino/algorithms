#!/bin/python
import sys

number = int(sys.argv[1])


def is_prime(number_a):
    for number_b in range(2, number_a):
        if not number_a % number_b:
            return False
    return True


if __name__ == '__main__':
    print(f'{number} is {"not" if not is_prime(number) else ""} a prime!')
