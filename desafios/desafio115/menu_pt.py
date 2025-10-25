import cadastrar
import listar

cores = { 'amarelo': '\033[33m',
          'limpa': '\033[m',
          'azul': '\033[34m',
          'vermelho_back': '\033[30;41m',
          }

def selecionaOpcao():
    while True:
        print('-' * 60)
        print(f'{"MENU PRINCIPAL":^60}')
        print('-' * 60)
        print('{}1{} - {} Ver pessoas cadastradas{}'.format(cores['amarelo'], cores['limpa'], cores['azul'],
                                                            cores['limpa']))
        print('{}2{} - {} Cadastrar nova Pessoa{}'.format(cores['amarelo'], cores['limpa'], cores['azul'],
                                                          cores['limpa']))
        print('{}3{} - {} Sair do Sistema{}'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
        print('-' * 60)
        opcao = int(input(f'{cores['amarelo']}Sua Opção: {cores['limpa']}'))
        if not 1 <= opcao <= 3:
            print('-' * 60)
            print(f'{cores['vermelho_back']}Opção Inválida!{cores['limpa']}')
            continue
        if opcao == 1:
            listar.listarNomes()
        elif opcao == 2:
            cadastrar.cadastrarNome()
        elif opcao == 3:
            break