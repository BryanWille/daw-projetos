print("Loja de Tinta Suvenir")

tamanho = float(input("Digite o tamanho da parede em m²: "))

# 1 Litro == 3m²
# 18 Litros = R$80,00

quantLitros = tamanho / 3
quantLatas = quantLitros / 18

if quantLitros % 18 > 1 and quantLatas % 18 > 0:
    quantLatas = int(quantLatas)
    quantLatas += 1

preco = quantLatas * 80
print(f"Tem que se comprar {quantLatas}, resultando no valor total fica: R${preco}")
