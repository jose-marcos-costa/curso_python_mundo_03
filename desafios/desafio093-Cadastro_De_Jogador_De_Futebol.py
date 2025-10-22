dados = dict()
gols = list()
dados['nome'] = str(input('Nome: ')).strip()
num_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(0, num_partidas):
    cada_partida = int(input(f'Quantos gols na partida {i}? '))
    gols.append(cada_partida)
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados['nome']} jogou {len(dados['gols'])} partidas.')
for p, g in enumerate(gols):
    print(f'\t=> Na partida {p}, fez {g} gols')
print(f'Foi um total de {dados["total"]} gols.')
print('-=' * 30)
