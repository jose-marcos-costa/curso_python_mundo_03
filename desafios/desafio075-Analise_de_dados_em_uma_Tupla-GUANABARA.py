digitados = ( int(input('Digite o 1º valor: ')),
        int(input('Digite o 2º valor: ')),
        int(input('Digite o 3º valor: ')),
        int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {digitados}')
print(f'O número 9 apareceu {digitados.count(9)} vezes')
if 3 in digitados:
    print(f'O primeiro valor 3 foi digitado na {digitados.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram: ', end='')
for n in digitados:
    if n % 2 == 0:
        print('{}'.format(n), end=' ')