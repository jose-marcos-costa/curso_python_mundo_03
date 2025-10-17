from random import randint
numeros = (randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO menor valor é {min(numeros)}')
print(f'O maior valor é {max(numeros)}')