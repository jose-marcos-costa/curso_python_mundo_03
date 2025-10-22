def escreva(txt):
    tam = len(txt) + 4
    print('~' * (tam))
    print(f'{txt:^{tam}}')
    print('~' * (tam))


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')