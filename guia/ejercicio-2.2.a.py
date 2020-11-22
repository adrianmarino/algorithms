#!/bin/python
import sys


def is_prime(number_a):
    for number_b in range(2, number_a):
        if not number_a % number_b:
            return False
    return True


if __name__ == '__main__':
    n = int(sys.argv[1])

    primes = [str(number) for number in range(1, n + 1) if is_prime(number)]

    print(', '.join(primes))
