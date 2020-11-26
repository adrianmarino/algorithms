def fahr_to_cel(fahr):
    return (5 * (fahr - 32)) / 9


def show(fahr, cel):
    print(f'{fahr} ºF -> {cel:.1f} ºC')


def fahr_to_cel_table(fahr, step, max):
    i = fahr
    while i <= max:
        show(i, fahr_to_cel(i))
        i += step


fahr_to_cel_table(0, 20, 100)
print()
fahr_to_cel_table(101, 1, 110)
