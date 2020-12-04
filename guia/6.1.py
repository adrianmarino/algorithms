#!/bin/python
"""
Programar las siguientes funciones recursivas en Python:

(a) pot_dos(n), que dado un número n ∈ N calcúle 2 elevado a la n . Ayuda: 2 a la 0 = 1.
(b) pot_a(a, n), que dados a, n ∈ N calcule a elevado a la n .
"""
import sys


def power_of(number, power):
    """
    Order: O(n)
    """
    if power == 0:
        return 1
    else:
        return number * power_of(number, power - 1)


number, power = int(sys.argv[1]), int(sys.argv[2])
print(f'{number}^{power} => {power_of(number, power)}')
