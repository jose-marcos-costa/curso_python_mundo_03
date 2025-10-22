from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'\t{k} tirou {v} no dado')
    sleep(0.5)
ordenado = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
print('-=' * 30)
print('Ranking dos jogadores:')
cont = 1
for k, v in ordenado.items():
    print(f'\t{cont}º Lugar: {k} com {v}')
    cont += 1
    sleep(0.5)