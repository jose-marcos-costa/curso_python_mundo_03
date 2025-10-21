from random import randint
from time import sleep
jogadores = {'jogador1': 0,
             'jogador2': 0,
             'jogador3': 0,
             'jogador4': 0}
print('Valores sorteados:')
for i in range (1, 5):
    chave = 'jogador' + str(i)
    jogadores[chave] = randint(1, 6)
    print(f'\t{chave} = {jogadores[chave]}')
    sleep(0.5)

ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print('-=' * 30)
print('Ranking dos jogadores:')
cont = 1
for k, v in ordenado.items():
    print(f'\t{cont}º Lugar: {k} com {v}')
    cont += 1
    sleep(0.5)