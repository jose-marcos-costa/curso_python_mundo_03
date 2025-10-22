from random import randint
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]} ', end= '')
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


# Programa Principal
sorteia(numeros)
# print(numeros)
somaPar(numeros)

