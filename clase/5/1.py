#!/bin/python
"""
Ejercicio 1: Usando el TAD Pila implementar una función reversa que dada una lista de vuelta sus elementos.

             Por ejemplo:
                - [1,2,3,4] → [4,3,2,1]
                - [] → []
                - [3] → [3]
"""


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def get(self):
        return self.stack[len(self.stack) - 1]


def reserve(numbers):
    stack = Stack()
    [stack.push(n) for n in numbers]

    result = []
    while not stack.is_empty():
        result.append(stack.get())
        stack.pop()

    return result


numbers = list(range(1, 5))
assert reserve(numbers) == numbers[::-1]

assert reserve([]) == []

assert reserve([3]) == [3]
