#!/bin/python


def reserve(string):
    """
    Order: O(n)
    """
    reserved_string = ''
    index = len(string) - 1
    while index >= 0:
        reserved_string += string[index]
        index -= 1
    return reserved_string


if __name__ == '__main__':
    text = "!ecneics retupmoc nioj"
    print(reserve(text))
