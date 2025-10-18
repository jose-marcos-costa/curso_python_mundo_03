matriz = [[], [], []]
soma_pares = maior_segunda = soma_terceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(num)
        if num % 2 == 0:
            soma_pares += num
        if j == 2:
            soma_terceira += num
        if i == 1 and num > maior_segunda:
            maior_segunda = num
print('-=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print('')
print('-=' * 40)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {maior_segunda}.')