geral = list()
dados = list()
auxiliar = list()
mais_pesadas = list()
mais_leves = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    geral.append(dados[:]) # Cópia!!!
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print(f'Foram cadastradas {len(geral)} pessoa(s)')
for pos, valor in enumerate(geral):
    if pos == 0:
        maior = valor[1]
        menor = valor[1]
    else:
        if valor[1] > maior:
            maior = valor[1]
        elif valor[1] < menor:
            menor = valor[1]
# print(maior)
# print(menor)
for v in geral:
    if v[1] == maior:
        mais_pesadas.append(v[0])
    elif v[1] == menor:
        mais_leves.append(v[0])
print(f'O maior peso foi {maior:.1f}Kg. Peso de {mais_pesadas}')
print(f'O menor peso foi {menor:.1f}Kg. Peso de {mais_leves}')
