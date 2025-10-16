# Texto para atualizar
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)
while True:
    teclado = int(input('Digite um número [0 a 20]: '))
    if 0 <= teclado <= 20:
        break
    print(f'Número Inválido!')
print(f'Você digitou o número {numeros[teclado]}')
