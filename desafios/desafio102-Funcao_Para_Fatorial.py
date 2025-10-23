def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
    else:
        for c in range(num, 0, -1):
            f *= c
            if c == 1:
                print(f'{c}', end=' ')
            else:
                print(f'{c}', end=' x ')
        print(f'= ', end='')
    return f


# Programa Principal
print(fatorial(5))
print('-' * 40)
help(fatorial)