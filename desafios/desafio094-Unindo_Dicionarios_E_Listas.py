pessoa = dict()
grupo = list()
soma_idade = media_idade = 0
cria_nome = ''
cont = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(grupo)}.')
print(f'- As mulheres cadastradas foram: ', end='')
for i, p in enumerate(grupo):
    soma_idade += grupo[i]['idade']
    if grupo[i]['sexo'] == 'F':
        print(grupo[i]['nome'],end=' ')
print()
media_idade = soma_idade / len(grupo)
print(f'- A média de idade é {media_idade}')
print(f'- Lista de pessoas que estão acima da média:')
for p in grupo:
    print()
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f' {k} = {v}', end=';')
print()
print('-=' * 30)
print('<<< ENCERRADO >>>')
