#!/bin/python
import sys


def is_prime(number_a):
    for number_b in range(2, number_a):
        if not number_a % number_b:
            return False
    return True


number = int(sys.argv[1])


print(f'{number} {"is" if is_prime(number) else "not is"} prime')
