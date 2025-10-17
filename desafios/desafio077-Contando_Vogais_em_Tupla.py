palavras = (
    'AVIAO',
    'CASA',
    'FUTEBOL',
    'MERCADO',
    'JANELA',
    'ESCOLA',
    'FLORESTA',
    'GATO',
    'ESTACAO',
    'VIAGEM'
)
for c in palavras:
    print(f'\nNa palavra {c} temos ', end=' ')
    for letra in c.lower():
        if letra in 'aeiou':
            print(f'{letra}', end=' ')

