#!/bin/python
import sys


def horizontal_line(times, char='*'):
    """
    Order: O(n)
    """
    output = ''
    for _ in range(0, times):
        output += char
    return output


class Square:
    def __init__(
            self,
            size=5,
            top_left=u'\u2554',
            top_right=u'\u2557',
            button_left=u'\u255a',
            button_right=u'\u255d',
            hor=u'\u2550',
            ver=u'\u2551'
    ):
        self.size = size
        self.top_left = top_left
        self.top_right = top_right
        self.button_left = button_left
        self.button_right = button_right
        self.hor = hor
        self.ver = ver

    def __draw_line_with_borders(self, left_border, right_border):
        return left_border + horizontal_line(self.size - 2, char=self.hor) + right_border + '\n'

    def draw(self):
        output = self.__draw_line_with_borders(self.top_left, self.top_right)

        for _ in range(0, self.size - 2):
            output += self.__draw_vertical_row()

        return output + self.__draw_line_with_borders(self.button_left, self.button_right)

    def __draw_vertical_row(self):
        output = self.ver
        for _ in range(0, self.size - 2):
            output += ' '
        output += self.ver + '\n'
        return output


if __name__ == '__main__':
    size = int(sys.argv[1])
    print(Square(size).draw())
