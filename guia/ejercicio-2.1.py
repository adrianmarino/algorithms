#!/bin/python
import sys

ONE_KM = 1.61


def is_not_blank(value):
    return value is not None and len(value) > 0


def assert_exist_param(position, name):
    assert len(sys.argv) - 1 >= position, f'Not found {name} parameter!'


def assert_is_not_blank(value, name):
    assert is_not_blank(value), f'A {name} is required!'


def asset_is_numeric(value, name):
    assert value.isnumeric(), f"A numeric {name} value is required!"


def get_required_param(name, position):
    assert_exist_param(position, name)
    param = sys.argv[position]
    assert_is_not_blank(param, name)
    return param


def get_required_numeric_param(name, position):
    param = get_required_param(name, position)
    asset_is_numeric(param, name)
    return float(param)


def get_optional_numeric_param(position, default=0):
    if not len(sys.argv) - 1 >= position:
        return default
    param = sys.argv[position]

    return float(param) if is_not_blank(param) and param.isnumeric() else default


def mi_to_km(value): return value * ONE_KM


def show_table(table, head, get_values):
    print(f'-------------------\n{head}\n-------------------')
    for row in table:
        values = get_values(row)
        print(f'{values[0]:.0f} -> {values[1]:.0f}')


if __name__ == '__main__':
    max_miles = get_required_numeric_param(name='max miles', position=1)
    step = get_optional_numeric_param(position=2, default=10)

    times = int(max_miles // step)
    if times == 0:
        exit(0)

    table = []
    for i in range(1, times + 1):
        miles = i * step
        table.append((miles, mi_to_km(miles)))

    show_table(table, "Miles -> Kilometers", lambda row: (row[0], row[1]))
    show_table(table, "Kilometers -> Miles", lambda row: (row[1], row[0]))
