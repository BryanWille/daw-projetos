cpf = str(input("Digite o CPF (###.###.###-##): "))
vetor_cpf = []
for c in cpf:
    if c.isdigit():
        vetor_cpf.append(int(c))

soma_cpf_um = soma_cpf_dois = 0
multiplicador = 10

for c in range(0, 9):
    soma_cpf_um += (vetor_cpf[c] * (10-c))

for c in range(0, 10):
    soma_cpf_dois += (vetor_cpf[c] * (11 - c))

verificador1 = (soma_cpf_um * 10) % 11
verificador2 = (soma_cpf_dois * 10) % 11


if verificador1 == int(cpf[len(cpf)-2]) and verificador2 == int(cpf[len(cpf)-1]):
    print(f"O seu CPF {cpf} é SIM válido!")
else:
    print(f"O seu CPF {cpf} NÂO é válido!")

print("Fim")
