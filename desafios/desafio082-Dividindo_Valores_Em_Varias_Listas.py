numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'NS':
            break
    if opcao == 'N':
        break
impares = []
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')