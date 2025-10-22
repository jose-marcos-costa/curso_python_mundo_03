def teste():
    x = 8   # Escopo Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função texte, x vale {x} ')

# Programa Principal
n = 2   # Escopo Global
print(f'No programa principal, n vale {n}')

teste()