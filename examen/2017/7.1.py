#!/bin/python

def more_frequently_element(elements):
    """
    Returns more more frequently element along with its frequency.

    Precondition: 'elements' is an ascending ordered numeric list.

    Example:

    elements  =  [1, 2, 4, 4]

    -------------------
    i  Max  curr, next
    -------------------
    0  1    1     2
    1  1    2     4
    2  1    4     4
    3  2    4     None
    -------------------

    """
    more_freq_element = None
    max_frequency = count = i = 0

    while i < len(elements):
        current_element = elements[i]
        next_element = elements[i + 1] if i + 1 < len(elements) else None
        i += 1

        count += 1

        if next_element != current_element:
            if count > max_frequency:
                max_frequency = count
                more_freq_element = current_element
            count = 0

    return more_freq_element, max_frequency


if __name__ == '__main__':
    ordered_numbers = [1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7, 4, 4, 4, 4]

    element, frequency = more_frequently_element(ordered_numbers)

    print(f'\nMore frequently element: {element}, Frequency: {frequency}')
