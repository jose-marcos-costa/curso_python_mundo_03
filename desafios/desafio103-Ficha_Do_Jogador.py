def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    g = int(g)
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    print('-' * 40)


# Programa Principal
print('-' * 40)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: ')).strip()
ficha(nome, gols)
