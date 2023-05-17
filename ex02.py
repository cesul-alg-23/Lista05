x = int(input('Informe um número inteiro'))

if x >= 0:
    # x elevado a 1/2, ou seja, raíz quadrada
    resultado = x ** 0.5
else:
    resultado = x ** 2

print(f'O resultado é {resultado}')
