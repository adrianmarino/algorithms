#!/bin/python
import sys


def is_not_blank(value):
    return value is not None and len(value) > 0


class Assert:
    @staticmethod
    def is_not_blank(value, name):
        assert is_not_blank(value), f'A {name} is required!'

    @staticmethod
    def has_params(position, name):
        assert len(sys.argv) - 1 >= position, f'Not found {name} parameter!'

    @staticmethod
    def is_numeric(value, name):
        assert value.isnumeric(), f"A numeric {name} value is required!"


class Input:
    @staticmethod
    def get_required_param(name, position):
        Assert.has_params(position, name)
        param = sys.argv[position]
        Assert.is_not_blank(param, name)
        return param

    @staticmethod
    def get_required_numeric_param(name, position):
        param = Input.get_required_param(name, position)
        Assert.is_numeric(param, name)
        return float(param)

    @staticmethod
    def get_optional_numeric_param(position, default=0):
        if not len(sys.argv) - 1 >= position:
            return default
        param = sys.argv[position]

        return float(param) if is_not_blank(param) and param.isnumeric() else default


def mi_to_km(value): return value * 1.61


def show_table(table, head, get_row):
    print(f'-------------------\n{head}\n-------------------')
    for row in table:
        values = get_row(row)
        print(f'{values[0]:.0f} -> {values[1]:.0f}')


max_miles = Input.get_required_numeric_param(name='max miles', position=1)
step = Input.get_optional_numeric_param(position=2, default=10)

times = int(max_miles // step)
if times == 0:
    exit(0)

table = []
for i in range(1, times + 1):
    miles = i * step
    table.append((miles, mi_to_km(miles)))

show_table(table, head="Miles -> Kilometers", get_row=lambda row: (row[0], row[1]))
show_table(table, head="Kilometers -> Miles", get_row=lambda row: (row[1], row[0]))
