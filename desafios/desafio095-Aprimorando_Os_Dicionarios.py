dados = dict()
gols = list()
completo = list()
total_gols = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    num_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for i in range(0, num_partidas):
        cada_partida = int(input(f'Quantos gols na partida {i}? '))
        total_gols += cada_partida
        gols.append(cada_partida)
    dados['gols'] = gols[:]
    gols.clear()
    dados['total'] = total_gols
    total_gols = 0
    completo.append(dados.copy())
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
    print('-' * 30)
print('-=' * 30)
print(f'{"cod":^5} {"nome":^8} {"gols":^20} {"total":^5}')
for i, jog in enumerate(completo):
    print(f'{i:^5}', end='')
    for k, v in jog.items():
        if k == 'nome':
            print(f'{v:<16}', end='')
        elif k == 'gols':
            print(f'{v}', end='')
        elif k == 'total':
            print(f'{v:^5}', end='')
    print()
while True:
    opcao = int(input('Mostrar dados de qual jogador? '))
    if opcao == 999:
        print('Finalizando...')
        break
    if not 0 <= opcao < len(completo):
        print('-' * 30)
        print(f'Não existe jogador com código {opcao}! Tente novamente...')
        print('-' * 30)
        continue
    print(f'-- LEVANTAMENTO DO JOGADOR {completo[opcao]["nome"]} --')
    for i, g in enumerate(completo[opcao]['gols']):
        print(f'No jogo {i} fez {g} gols.')

