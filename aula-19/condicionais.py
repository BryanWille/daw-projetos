ladoA = float(input('Digite o primeiro lado: '))
ladoB = float(input('Digite o segundo lado: '))
ladoC = float(input('Digite o terceiro lado: '))

if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if (ladoA == ladoB) and (ladoA == ladoC):
        print('Triângulo Equilátero!')
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoC == ladoA):
        print('Triângulo Isósceles')
    else:
        print("Triângulo Escaleno")
else:
    print("Sua figura não é um triângulo!")
