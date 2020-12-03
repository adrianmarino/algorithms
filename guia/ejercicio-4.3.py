#!/bin/python


def max_plateau(numbers):
    """
    Order: O(n)
    """
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


def test(list, expected_element, expect_count):
    element, count = max_plateau(list)
    assert expected_element == element, f'Input: {list}, Element: {expected_element} != {element}'
    assert expect_count == count, f'Input: {list}, Max count: {expect_count} != {count}'
    print('Pass -> List:', list, 'element:', element, 'Max count:', count)


test([1, 1, 2, 6, 6, 6, 3, 3, 3, 3], expected_element=3, expect_count=4)
test([1, 1, 2, 6, 6, 6, 3, 3, 3], expected_element=6, expect_count=3)
test([], expected_element=None, expect_count=0)
test([1, 2, 3], expected_element=1, expect_count=1)
test([1, 2], expected_element=1, expect_count=1)
test([1, 1], expected_element=1, expect_count=2)
test([1], expected_element=1, expect_count=1)