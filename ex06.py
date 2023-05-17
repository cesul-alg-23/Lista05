lado_a = int(input('Informe o lado A: '))
lado_b = int(input('Informe o lado B: '))
lado_c = int(input('Informe o lado C: '))

if (lado_a + lado_b > lado_c) and \
        (lado_a + lado_c > lado_b) and \
        (lado_b + lado_c > lado_a):

    print("Os lados formam um triângulo")

    if (lado_a == lado_b) and (lado_a == lado_c):
        print("Triângulo equilátero!")
    elif (lado_a != lado_b) and (lado_a != lado_c) and (lado_b != lado_c):
        print("Triângulo escaleno!")
    else:
        print("Triângulo isósceles")

else:
    print("Os lados não formam um triângulo")


