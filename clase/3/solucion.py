###########################
########EJERCICIO 1########
###########################

import time


# busqueda lineal de x en l
def busquedaLineal(x, l):
    rv = -1
    i = 0
    while i < len(l):
        if l[i] == x:
            rv = i
        i = i + 1
    return rv


# busqueda binaria de x en l
def busquedaBinaria(x, l):
    rv = -1
    izq = 0
    der = len(l) - 1
    while izq < der:
        med = (izq + der) // 2
        if l[med] < x:
            izq = med + 1
        else:
            der = med
    if l[izq] == x:
        rv = izq
    return rv


# comparacion de tiempos de ejecucion entre ambas busquedas
print("\nEJERCICIO 1")
print("Busquedas sobre 41.450.000 (poblacion argentina aprox.)")
print("Iniciando busqueda lineal...")
t0 = time.time()
busquedaLineal(745, range(41450000))
tiempo = time.time() - t0
print("Busqueda lineal:", round(tiempo, 2), "seg.")

print("Iniciando busqueda binaria...")
t0 = time.time()
busquedaBinaria(745, range(41450000))
tiempo = time.time() - t0
print("Busqueda binaria:", round(tiempo, 2), "seg.\n\n")


###########################
########EJERCICIO 2########
###########################

# PRE: l1 y l2 estan ordenadas y no tienen elementos repetidos
# Devuelve la cantidad de elementos que aparecen en ambas listas
def enAmbasListas(l1, l2):
    rv = 0
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            rv = rv + 1
            i = i + 1
            j = j + 1
        elif l1[i] < l2[j]:
            i = i + 1
        else:
            j = j + 1
    return rv


print("EJERCICIO 2")
print(enAmbasListas([1, 2, 3, 4, 5], [1, 5, 6, 7, 8]))
print(enAmbasListas([5], [1, 6, 7, 8]))
print(enAmbasListas([1, 6, 7, 8], [1, 6, 7, 8]))
print("\n")


###########################
########EJERCICIO 3########
###########################

# PRE: los valores de l estan entre 0 y 9
def ordenar_digitos(l):
    # 1. para los numeros entre 0 y 9 contamos cuantos hay de cada uno en l
    cant = [0] * 10
    for i in range(len(l)):
        cant[l[i]] = cant[l[i]] + 1

    # 2. escribimos en orden la cantidad que habia de cada un en l
    pos = 0
    for i in range(10):
        for j in range(cant[i]):
            l[pos] = i
            pos = pos + 1


print("EJERCICIO 3")
l = [2, 3, 1, 3, 4, 5, 9, 6, 7, 4, 5, 3, 2, 0, 9, 7]
print(l)
ordenar_digitos(l)
print(l)
