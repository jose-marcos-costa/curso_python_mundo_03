expressao = []
expressao.append(str(input('Digite a expressão: ')).strip())
cont_abre = cont_fecha = 0
print(f'{expressao[0]}')
for v in expressao[0]:
    if v == '(':
        cont_abre += 1
    elif v == ')':
        cont_fecha += 1
# print(f'Abriu {cont_abre} vezes')
# print(f'Fechou {cont_fecha} vezes')
if cont_abre == cont_fecha:
    print(f'Sua expressão está certa!')
else:
    print(f'Sua expressão está errada!')


