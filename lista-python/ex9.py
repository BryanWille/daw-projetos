repeticao = 0
valores = []
while repeticao != -1:
    repeticao = int(input("Digite um valor: "))
    if repeticao != -1:
        valores.append(repeticao)

def valoresTotais():
    return len(valores)
def valoresOrdem():
    return valores
def valoresContrario():
    desordem = []
    for c in range(len(valores)-1, -1, -1):
        desordem.append(valores[c])
    return desordem
def somaTotal():
    soma_total = 0
    for v in valores:
        soma_total += v
    return soma_total
def media():
    return somaTotal() / len(valores)
def acimaMedia():
    acima_media = 0
    for v in valores:
        if v > media():
            acima_media += 1
    return acima_media
def menorSete():
    menor_sete = 0
    for v in valores:
        if v < 7:
            menor_sete += 1
    return menor_sete

menu = 0

while menu != -1:
    print("Quais informação quer saber?")
    print("[1] Quantidades de Valores"
          "\n[2] Todos os Valores"
          "\n[3] Todos os Valores ao Contrário"
          "\n[4] A soma de Todos os Valores"
          "\n[5] A média de Todos os Valores"
          "\n[6] Quantidade de Valores Acima da Média"
          "\n[7] Quantidade de Valores Menores que Sete"
          "\n[-1] Fechar o Programa")
    menu = int(input(">>> "))
    if menu != -1:
        print("\n")
        if menu == 1:
            print(f"Quantidades de valores lidos: {valoresTotais()} ")
        elif menu == 2:
            print(f"Valores informados: {valoresOrdem()}")
        elif menu == 3:
            print(f"Valores ao contrário: {valoresContrario()}")
        elif menu == 4:
            print(f"Soma total dos valores: {somaTotal()}")
        elif menu == 5:
            print(f"A média dos valores é: {media()}")
        elif menu == 6:
            print(f"Quantidade de valores acima da média: {acimaMedia()}")
        elif menu == 7:
            print(f"Quantidade de valores abaixo de sete: {menorSete()}")
        else:
            print("Opção Inválida!")
        print("\n")
print("Fim do Programa!")
