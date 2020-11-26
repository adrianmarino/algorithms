def fahr_to_cel(fahr): return (5 * (fahr - 32)) / 9


def show(fahr, cel): print(f'{fahr} ºF -> {cel:.1f} ºC')


fahr = 0
step = 10
max = 100
while fahr <= max:
    show(fahr, fahr_to_cel(fahr))

    print(f'{fahr} ºF -> {cel:.1f} ºC')
    fahr += step
