def es_par(numero):
    return numero % 2 == 0


def filtrar_pares(numeros):
    i = 0
    pares = []
    while i < len(numeros):
        numero = numeros[i]
        if es_par(numero):
            pares.append(numero)
        i = i + 1
    return pares


print(filtrar_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6])
print(filtrar_pares([]) == [])
print(filtrar_pares([1, 3, 5]) == [])
