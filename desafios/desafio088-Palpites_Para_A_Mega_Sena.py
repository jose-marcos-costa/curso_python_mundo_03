from time import sleep
from random import randint
jogos = list()
dados = list()
print('-' * 40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-' * 40)
vezes = int(input(f'Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {vezes} JOGOS')
for i in range(0, vezes):
    while len(dados) < 6:
        num = randint(1, 60)
        if num in dados:
            # print('Já tem...')
            continue
        else:
            dados.append(num)
    # print(dados)
    dados.sort()
    print(dados)
    jogos.append(dados[:])
    dados.clear()
    sleep(1)
print('{:=^40}'.format(' < BOA SORTE! >'))
