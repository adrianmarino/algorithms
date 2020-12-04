def prod(n, m):  # 5 + 10n (En esta función a la 'n' de pot la renombramos a 'm', Ojo! )
    """
    Orden: O(m)
    """
    i = 0  # 1
    multi = 0  # 1
    while i < m:  # 3
        multi = multi + n  # 4
        i = i + 1  # 3
    return multi


def pot(n, m):
    """
    Orden: O(m^n)
    """
    i = 0  # 1
    potencia = 1  # 1
    while i < m:  # 3
        potencia = prod(potencia, n)  # 5 + 10n
        i = i + 1  # 3
    return potencia


"""
Complejidad:

T = 1 + 1 + 3 + ((5 + 10n) + 3 +3 )*m
T = 5 + (11 + 10n)*m
T = 5 + 11m + 10(n*m)

=> O(n*m)
"""

print(pot(2, 10))
