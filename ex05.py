a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

if menor % 2 == 0:
    print(f'O menor valor é {menor}, ele é par!')
else:
    print(f'O menor valor é {menor}, ele é ímpar!')

