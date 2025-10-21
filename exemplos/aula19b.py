estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[:]) # Dicionários não aceitam cópias por fatiamento
    brasil.append(estado.copy())
print(brasil)
print(f'-=' * 30)
"""
for e in brasil:        # For para a lista
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
"""
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()