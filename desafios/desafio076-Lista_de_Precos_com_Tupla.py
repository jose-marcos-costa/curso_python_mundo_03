dados_supermercado = (
    'Pasta de dente 180g', 9.99,
    'Arroz Parboilizado 5kg', 24.50,
    'Leite Integral UHT 1L', 4.15,
    'Feijão Carioca 1kg', 8.75,
    'Óleo de Soja 900ml', 6.90,
    'Café Torrado e Moído 500g', 15.30,
    'Biscoito Salgado 350g', 3.49,
    'Sabão em Pó 1kg', 12.00,
    'Shampoo 300ml', 18.99,
    'Filé de Peito de Frango 1kg', 21.80
)
print('-' * 50)
print('{:^50}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 50)
for i in range(0, 20, 2):
    print('{:.<40} R$ {:>6.2f}'.format(dados_supermercado[i], dados_supermercado[i+1]))
print('-' * 50)