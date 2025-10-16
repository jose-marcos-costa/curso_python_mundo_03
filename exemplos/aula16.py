lanche = ('Burger', 'Juice', 'Pizza', 'Pudim', 'French Fries')


# lanche[3] = 'Brigadeiro'
# Tuplas são imutáveis
print(lanche[::-1])
print('-=' * 30)
print(lanche[-4])
print('-=' * 30)
print(lanche[-4:-1])
print('-=' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('-=' * 30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-=' * 30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(lanche)
print(sorted(lanche))