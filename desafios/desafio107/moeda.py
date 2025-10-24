def aumentar(preco, taxa):
    res = preco * (1 + taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco * ( 1 - taxa / 100)
    return res


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res
