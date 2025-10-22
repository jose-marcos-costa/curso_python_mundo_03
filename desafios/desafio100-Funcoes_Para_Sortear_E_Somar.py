from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]} ', end= '')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


# Programa Principal
numeros = list()
sorteia(numeros)
# print(numeros)
somaPar(numeros)

