def pyHelp():
    while True:
        imprimeColorido('SISTEMA DE AJUDA PyHELP', cores['amarelo_back'])
        opcao = str(input('Função ou Biblioteca> ')).strip()
        if opcao == 'SAIR':
            imprimeColorido('ATÉ LOGO!', cores['vermelho_back'])
            break
        frase = "Acessando o manual do comando/biblioteca '" + opcao + "'"
        imprimeColorido(frase, cores['azul_back'])
        help(opcao)

def imprimeColorido(f, cor):
    tam = len(f)+4
    print('{}'.format(cor), '~' * tam )
    print(f'   {f}')
    print('{}'.format(cor), '~' * tam )
    print('{}'.format(cores['limpa']))


# Programa Principal
cores = { 'amarelo_back': '\33[30;43m',
          'limpa': '\33[m',
          'azul_back': '\33[30;44m',
          'vermelho_back': '\33[30;41m',
          }
pyHelp()