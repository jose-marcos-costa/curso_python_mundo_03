num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
digitados = (num1, num2, num3, num4)
print(f'Você digitou os valores {digitados}')
print(f'O número 9 apareceu {digitados.count(9)} vezes')
try:
    digitados.index(3)
    print(f'O primeiro valor 3 foi digitado na {digitados.index(3) + 1}ª posição.')
except ValueError:
    print(f'O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram: ', end='')
for n in digitados:
    if n % 2 == 0:
        print('{}'.format(n), end=' ')