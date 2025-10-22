pessoa = dict()
grupo = list()
soma_idade = media_idade = 0
cria_nome = ''
cont = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas cadastradas.')
media_idade = soma_idade / len(grupo)
print(f'- A média de idade é {media_idade:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'],end=' ')
print()
print(f'- Lista de pessoas que estão acima da média:')
for p in grupo:
    print()
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f' {k} = {v}', end=';')
print()
print('-=' * 30)
print('<<< ENCERRADO >>>')
