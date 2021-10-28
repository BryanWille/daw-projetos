def converterSegundos(segundosTempo):
    segundos = (segundosTempo % 60)
    minutos = (segundosTempo % 3600) // 60
    horas = segundosTempo // 3600
    return f'{horas}:{minutos}:{segundos}'


distancia = int(input("Digite o tamanho do arquivo (em MB): "))
velocidade = int(input("Digite a velocidade da internet (em Mb): "))

tempo = distancia / (velocidade/8)
print(tempo)

print(f"O Tempo é: {converterSegundos(tempo)}")
