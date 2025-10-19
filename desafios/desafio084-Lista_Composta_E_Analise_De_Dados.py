geral = list()
dados = list()
mais_pesadas = list()
mais_leves = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    if len(geral) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:]) # Cópia!!!
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print(f'Foram cadastradas {len(geral)} pessoa(s)')
for v in geral:
    if v[1] == maior:
        mais_pesadas.append(v[0])
    elif v[1] == menor:
        mais_leves.append(v[0])
print(f'O maior peso foi {maior:.1f}Kg. Peso de {mais_pesadas}')
print(f'O menor peso foi {menor:.1f}Kg. Peso de {mais_leves}')
