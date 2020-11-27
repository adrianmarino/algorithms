#!/bin/python
import sys


def power_of(number, power):
    return number * (1 if power <= 1 else power_of(number, power - 1))


number, power = int(sys.argv[1]), int(sys.argv[2])
print(f'{number}^{power} => {power_of(number, power)}')
