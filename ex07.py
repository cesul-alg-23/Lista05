nota = float(input("Informe a nota do aluno: "))

if nota < 0 or nota > 10:
    print('Nota inválida!')
elif nota >= 9:
    print('Superior!')
elif nota >= 7:
    print('Médio Superior!')
elif nota >= 5:
    print('Médio!')
elif nota >= 3:
    print('Médio Inferior!')
elif nota >= 0.1:
    print('Inferior!')
else:
    print('Sem rendimento')
