#!/bin/python
def max_plateau(numbers):
    curr_number, max_number = None, 0
    max_count = curr_count = 0

    for number in numbers:
        if curr_number is None:
            curr_number = number

        if curr_number != number:
            if curr_count > max_count:
                max_count = curr_count
                max_number = curr_number

            curr_number = number
            curr_count = 0

        curr_count += 1

    return max_number, max_count


numbers = [1, 1, 2, 6, 6, 6, 3, 3]
num, long = max_plateau(numbers)
print(f'Max plateau -> num: {6} , long: {long} ')
