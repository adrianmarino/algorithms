"""
Ejercicio 1: Implementar en Python una función recursiva que dados dos números a y n.
"""
import sys


def power(num, num_power):
    return 1 if num_power == 0 else num + power(num, num_power - 1)


num, num_power = int(sys.argv[1]), int(sys.argv[2])
print(f'{num} ^ {num_power} -> {power(num, num_power)}')
