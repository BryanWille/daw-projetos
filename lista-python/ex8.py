valores = []
repeticao = soma_total = menor_sete = contador = acima_media = 0
while repeticao != -1:
    repeticao = int(input("Digite um valor: "))
    if repeticao != -1:
        contador += 1
        valores.append(repeticao)
        soma_total += repeticao
        if repeticao < 7:
            menor_sete += 1


media = soma_total / contador
vetor_contrario = []

for c in range(len(valores)-1, -1, -1):
    vetor_contrario.append(valores[c])
    if valores[c] > media:
        acima_media += 1


print(f"Quantidades de valores lidos: {contador} ")
print(f"Valores informados: {valores}")
print(f"Valores ao contrário: {vetor_contrario}")
print(f"Soma total dos valores: {soma_total}")
print(f"A média dos valores é: {media}")
print(f"QUantidade de valores acima da média: {acima_media}")
print(f"Quantidade de valores abaixo de sete: {menor_sete}")
print("Programa Encerrado!")
