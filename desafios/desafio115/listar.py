def listarNomes():
    print('-' * 60)
    print(f'{"PESSOAS CADASTRADAS":^60}')
    print('-' * 60)
    with open("listaDeNomes.txt", 'r') as arquivo:
        for linha in arquivo:
            linha = str(linha).strip()
            nome = linha.split('|')[0].strip()
            idade = int(linha.split('|')[1].strip())
            print(f'{nome:<50}{idade:>5} anos')