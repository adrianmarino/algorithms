#!/bin/python
"""
Dada una lista de 1s y 0s representando un número en base binaria, obtener el número correspondiente en base decimal.

Order: O(n)
"""


def bin_to_dec(binary):
    """
    Order: O(n)
    """
    if len(binary) == 1:
        return binary[0]  # == 2 ** 0 + binary[0]
    else:
        return 2 ** (len(binary) - 1) * binary[0] + bin_to_dec(binary[1:])


binary = [1, 1, 0, 0, 1]  # 25
print(f'Binary: {binary} --> Natural: {bin_to_dec(binary)}')

binary = [1, 1, 0, 1]  # 13
print(f'Binary: {binary} --> Natural: {bin_to_dec(binary)}')

binary = [1, 0, 0, 1]  # 9
print(f'Binary: {binary} --> Natural: {bin_to_dec(binary)}')
