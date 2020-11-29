#!/bin/python


def max_plateau(numbers):
    max_num = None
    max_count = count = i = 0

    while i < len(numbers):
        cur_num = numbers[i]
        next_num = numbers[i + 1] if i + 1 < len(numbers) else None

        count += 1

        if next_num != cur_num:
            if count > max_count:
                max_count = count
                max_num = cur_num
            count = 0

        i += 1

    return max_num, max_count


numbers = [1, 1, 2, 6, 6, 6, 3, 3, 3, 3]
num, long = max_plateau(numbers)
print(f'Max plateau -> num: {num} , long: {long} ')
