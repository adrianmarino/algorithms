#!/bin/python

def max_plateau(list):
    element = None
    index = max_count = curr_count = 0

    while index < len(list):
        curr_count += 1

        current = list[index]
        next = list[index + 1] if index + 1 < len(list) else None
        index += 1

        if current != next:
            if curr_count > max_count:
                element = current
                max_count = curr_count
            curr_count = 0

    return element, max_count


def assert_equal(expected_value, current_value, label):
    assert expected_value == current_value, f'{label}: {expected_value}(expected) != {current_value}'


def test(list, expected_element, expected_count):
    element, count = max_plateau(list)
    assert_equal(expected_element, element, 'Input: {list}, Element')
    assert_equal(expected_count, count, 'Input: {list}, Macx count')
    print(f'Test pass -> Input: {list}, Element: {element}, Max count: {count}.')


test([1, 1, 2, 6, 6, 6, 3, 3, 3, 3], 3, 4)
test([1, 1, 2, 6, 6, 6, 3, 3, 3], 6, 3)
test([], None, 0)
test([1, 2, 3], 1, 1)
test([1, 2], 1, 1)
test([1, 1], 1, 2)
test([1, 1, 1], 1, 3)
test([1], 1, 1)
