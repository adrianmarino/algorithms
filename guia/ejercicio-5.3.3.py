#!/bin/python
import sys


def is_prime(number):
    """
    Order: O(n ** 1/2)
    """
    for num in range(2, round(number ** 0.5)):
        if not num % number:
            return False
    return True


number = int(sys.argv[1])
print(f'{number} {"is" if is_prime(number) else "not is"} prime')
