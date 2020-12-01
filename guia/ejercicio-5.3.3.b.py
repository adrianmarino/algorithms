#!/bin/python
"""
Los números primos son numeros que son divisibles por uno y por sí mismos.
Si es divisible por otro numero entre 2 y raiz(n) entonces no es primo.
"""


def is_divisible_by(number, divider):
    return number % divider == 0


def is_prime(number):
    """
    Order: O(sqrt(n))
    """
    return is_prime_aux(number, range(2, int(number ** 0.5) + 1))


def is_prime_aux(number, dividers):
    if len(dividers) == 0:
        return True
    else:
        return not is_divisible_by(number, dividers[0]) and is_prime_aux(number, dividers[1:])


# Primes: 2, 3, 5, 7, 11, 13, 17
for number in range(2, 15):
    print(f'- {number} {"is" if is_prime(number) else "is not"} prime')
