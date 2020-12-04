#!/bin/python
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Name argument is required!")
        exit(1)

    name = sys.argv[1]

    print(f'Hello {name}')
