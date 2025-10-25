cores = { 'amarelo_back': '\033[30;43m',
          'limpa': '\033[m',
          'azul_back': '\033[30;44m',
          'vermelho_back': '\033[30;41m',
          }

def leiaDinheiro(msg):
    valido = False          # Flag
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('{}ERRO: \"{}\" é um preço inválido!{}'.format(cores['vermelho_back'], entrada, cores['limpa']))
        else:
            valido = True
            return float(entrada)