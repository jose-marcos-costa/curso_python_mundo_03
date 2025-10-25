def cadastrarNome():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    print('-' * 60)
    with open("listaDeNomes.txt", 'a') as arquivo:
        nova_linha = f'\n{nome} | {idade}'
        arquivo.write(nova_linha)
    print(f'Novo registro de {nome} adicionado.')