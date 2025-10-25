def aumentar(preco = 0, taxa = 0, formato=False ):
    res = preco * (1 + taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco * ( 1 - taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')


def resumo(preco = 0, taxa_aum = 0, taxa_red = 0):
    print('~' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('~' * 30)
    print(f'{"Preço analisado:":<20}{moeda(preco):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(preco, True)}')
    print(f'{"Metade do preço:":<20}{metade(preco, True)}')
    print(f'{taxa_aum:<3}{"% de aumento:":<17}{aumentar(preco, taxa_aum, True):>10}')
    print(f'{taxa_red:<3}{"% de redução:":<17}{diminuir(preco, taxa_red, True):>10}')
    print('~' * 30)
