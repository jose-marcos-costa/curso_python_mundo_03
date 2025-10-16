numeros = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)
teclado = int(input('Digite um número [0 a 20]: '))
while teclado < 0 or teclado > 20:
    print(f'Número Inválido!')
    teclado = int(input('Digite um número [0 a 20]: '))
print(numeros[teclado])
