"""
Ejercicio 2: Usando el TAD Pila implementar una función que dado un String que contiene una única aparición
             del caracter '#' determine si es o no capicua:
              - 'abc#cba' → True
              - 'abba#abb' → False
              - '#' → True
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
    for n in numbers:
        stack.push(n)

    result = []
    while not stack.is_empty():
        result.append(stack.get())
        stack.pop()

    return result


def join(char_list):
    word = ''
    for char in char_list:
        word += char
    return word


def is_palindrome(word):
    return word == join(reserve(word))


assert is_palindrome('abc#cba')
assert not is_palindrome('abba#abb')
assert is_palindrome('#')
