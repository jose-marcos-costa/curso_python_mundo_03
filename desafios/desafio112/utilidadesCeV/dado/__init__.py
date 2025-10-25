cores = { 'amarelo_back': '\033[30;43m',
          'limpa': '\033[m',
          'azul_back': '\033[30;44m',
          'vermelho_back': '\033[30;41m',
          }


def leiaDinheiro(msg):
    preco = str(input(msg))
    cont_virg = 0
    cont_pont = 0
    for c in preco:
        if c == '.':
            cont_pont += 1
            print('Tem ponto')
        elif c == ',':
            cont_virg += 1
            print('Tem vírgula')
    if cont_pont > 0 and cont_virg > 0:
        print('{}ERRO: "{}" é um preço inválido! Vírgula e ponto ao mesmo tempo!{}'.format(cores['vermelho_back'], preco, cores['limpa']))
    if cont_pont == 0 and cont_virg == 0 and preco.isnumeric():
        resp = int(preco)
        return resp
    if cont_virg > 0 and cont_pont == 0:
        resp = float(preco.replace(',', '.'))
        return resp
    if cont_pont > 0 and cont_virg == 0:
        resp = float(preco)
        return resp
    if preco.isspace():
        print('{}ERRO: "{}" é um preço inválido! Somente espaçoes foram digitados!{}'.format(cores['vermelho_back'], preco, cores['limpa']))