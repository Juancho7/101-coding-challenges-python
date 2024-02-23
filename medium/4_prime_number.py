"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

for i in range(2, 101):
    dividers = 2

    for j in range(2, i):
        if i % j == 0:
            dividers += 1

    if dividers == 2:
        print(i)
    else:
        continue
