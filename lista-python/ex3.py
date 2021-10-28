def statusAluno(nota1, nota2):
    stats = 0
    media = (nota1 + nota2) / 2
    if media == 10:
        status = "Aprovado Com Distinção"
    elif media >= 7:
        status = "Aprovado!"
    else:
        status = "Reprovado!"
    return status


nota = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
print(statusAluno(nota, nota2))
