tabela_brasileirao = (
    'Palmeiras',
    'Flamengo',
    'Cruzeiro',
    'Mirassol',
    'Botafogo',
    'Bahia',
    'Fluminense',
    'São Paulo',
    'Vasco',
    'Bragantino',
    'Ceará',
    'Corinthians',
    'Grêmio',
    'Atlético-MG',
    'Internacional',
    'Santos',
    'Vitória',
    'Fortaleza',
    'Juventude',
    'Sport'
)
"""
for pos,time in enumerate(tabela_brasileirao):
    print(f'{pos+1}º colocado | {time}')
"""
print('=' * 40)
print(f'Lista de Times do Brasileirão: {tabela_brasileirao}')
print('=' * 40)
print(f'Os 5 primeiros são: {tabela_brasileirao[:5]}')
print('=' * 40)
print(f'Os 4 últimos são {tabela_brasileirao[16:]}')
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('=' * 40)
print(f'O Bahia está na {tabela_brasileirao.index('Bahia')}ª posição.')