expressao = str(input('Digite a expressão: '))
pilha = []
for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está errada!')


