a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if a > b and a > c:
    print(f'O maior valor é {a}')
elif b > a and b > c:
    print(f'O maior valor é {b}')
else:
    print(f'O maior valor é {c}')
