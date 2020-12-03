#!/bin/python

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


def index_of(list, element):
    i = 0
    while i < len(list):
        if list[i] == element:
            return i
        i += 1
    return -1


OPEN = ['(', '[', '{']
CLOSE = [')', ']', '}']


def balanced(string):
    stack = Stack()
    for char in string:
        if index_of(OPEN, char) > -1:
            stack.push(char)
        else:
            index = index_of(CLOSE, char)
            if index > -1:
                if stack.get() == OPEN[index]:
                    stack.pop()
                else:
                    return False

    return stack.is_empty()


assert balanced('safdsad')
assert balanced('[]')
assert balanced('[{()}]')
assert not balanced('([)]')
assert not balanced('[{)(}]')
