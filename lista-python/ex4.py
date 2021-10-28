def novoSalario(salario):
    salarioAntes = salario
    if salario <= 280:
        salario *= 1.20
        percentual = '20%'
    elif salario < 700:
        salario *= 1.15
        percentual = '15%'
    elif salario < 1500:
        salario *= 1.10
        percentual = '10%'
    else:
        salario *= 1.05
        percentual = '5%'
    aumento = salario - salarioAntes
    print(f"Salário Antes: {salarioAntes}, Percentual Aplicado: {percentual},"
          f"\nValor do Aumento: {aumento}, Novo Salário: {salario}")


salario = float(input("Digite o Salário: "))
novoSalario(salario)
