lista = list()
dados = list()
notas = list()
while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    media = (n1 + n2) / 2
    dados.append(notas[:])
    notas.clear()
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao in 'N':
        break
print('-=' * 50)
print('{:^5}'.format('Nº'), end='')
print('{:<20}'.format('NOME'), end='')
print('{:<10}'.format('MÉDIA'))
print('-' * 40)
for pos, valor in enumerate(lista):
    print(f'{pos:<4} {valor[0]:<20} {valor[2]:<10}')
print('-' * 40)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    print(f'Notas da {lista[aluno][0]} são {lista[aluno][1]}')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')